.. title: Simple Binder usage with Sphinx-Gallery through Jupytext
.. slug: simple-binder-usage-with-sphinx-gallery-through-jupytext
.. date: 2019-07-06 16:00:00 UTC+02:00
.. tags: python, sphinx, plasmapy
.. category: 
.. link: 
.. description: 
.. type: text

It's been a busy week for `PlasmaPy <https://github.com/PlasmaPy/PlasmaPy/>`_. I recently found out about Binder support in `sphinx-gallery <https://sphinx-gallery.github.io/>`_. The latter is a package that we use to
turn python scripts with comments into Sphinx pages and Jupyter Notebooks. I figured adding that could be a nice fit for `our existing example gallery <http://docs.plasmapy.org/en/stable/auto\_examples/index.html>`_ .

However, I quickly realized that the system in place is a bit unwieldy. Binder takes a link to an existing GitHub repository and executes ``.ipynb`` notebooks located there online. However, with sphinx-gallery, we don't have those notebooks in the repository - we have ``.py`` files with comments. `The currently recommended way of setting this up with sphinx-gallery <https://sphinx-gallery.github.io/configuration.html#binder-links>`_ is keeping your built documentation in `another repository <https://github.com/sphinx-gallery/sphinx-gallery.github.io>`_ and hosting it via something along the lines of GitHub Pages rather than `ReadTheDocs <https://readthedocs.org/>`_, which we are currently using.

`I added the results of this investigation to sphinx-gallery's docs <https://github.com/sphinx-gallery/sphinx-gallery/pull/505/files>`_, but I didn't want to switch away from RTD, so I figured I'd go ahead and find another way. I think I've got something that works well enough now!

Trigger warning: later on during this post, there may be monkeypatching of sphinx_gallery internals. Beware.

.. TEASER_END

Using Jupytext
==============

`The Jupytext project <https://github.com/mwouts/jupytext/>`_ is kind of like `nbconvert <https://github.com/jupyter/nbconvert>`_, but two-way. It lets you turn notebooks into scripts and vice versa. The interesting thing is that, `as per Jupytext's documentation <https://jupytext.readthedocs.io/en/latest/formats.html#sphinx-gallery-scripts>`_, it is possible to let Binder's jupyter instance parse sphinx-gallery style ``.py`` files as jupyter notebooks. This was done in `PlasmaPy#656 <https://github.com/PlasmaPy/PlasmaPy/pull/656/files>`_ . First, let's instruct the in-binder Jupyter instance to parse ``.py`` files in ``.jupyter/jupyter_notebook_config.py`` via blatant copy-paste:

.. code:: python

	c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
	c.ContentsManager.preferred_jupytext_formats_read = "py:sphinx"
	c.ContentsManager.sphinx_convert_rst2md = True

And then let's also add a ``binder/requirements.txt`` file that lets Binder know what Python packages to download while building the repository's image. The version I had there was pretty shoddy, as CI/``setup.py``/packaging errors surfaced while I was tinkering with this. Long story short, something like this should do:

.. code::

    -r ../requirements/automated-documentation-tests.txt
    jupytext
    .

Where, in didactic order:

* ``jupytext`` should be pretty self-explanatory,
* ``.`` is the repository's package itself (here, PlasmaPy), as accessed by ``setup.py``
* ``-r ../requirements/automated-documentation-tests.txt`` reads a pip requirements file specifying our documentation requirements. I think with a proper ``extras_require`` specified in ``setup.py``, these two lines could be collapsed simply into ``.[dev]`` or some such. Note that ``-r`` takes a path relative to the file, thus the ``../``

At this point all this really is is implementing what's mentioned in Jupytext's docs. The result is as follows:

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/PlasmaPy/PlasmaPy/master?filepath=plasmapy%2Fexamples
 :align: center

But you might notice an inconsistency in the Sphinx-rendered gallery itself: even if we were to `configure docs to display Binder links <https://sphinx-gallery.github.io/configuration.html#binder-links>`_ they will point to a path as imagined by the current implementation in Sphinx-Gallery, such as:

.. code::

    https://gke.mybinder.org/v2/gh/PlasmaPy/PlasmaPy/master?filepath=plasmapy/examples/auto_examples/plot_physics.ipynb

Note the spurious ``auto_examples`` directory supposedly including an ``.ipynb`` file. This obviously doesn't work for our use case, so we'd like to be able to change the generated links somehow...

Monkeypatching
==============

This (or rather, `PlasmaPy#658 <https://github.com/PlasmaPy/PlasmaPy/pull/658/files>`_ ) is where it gets dirty. The solution developed in cooperation with Stuart Mumford (of SunPy fame, who contributed the idea which I implemented) is monkeypatching sphinx-gallery's link generation code. It's simple, yet effective.

Let's use this config for ``sphinx-gallery``:

.. code:: python

	sphinx_gallery_conf = {
		# path to your examples scripts
		'examples_dirs': '../plasmapy/examples',
		# path where to save gallery generated examples
		'backreferences_dir': 'gen_modules/backreferences',
		'gallery_dirs': 'auto_examples',
		'binder': {
			'org': 'PlasmaPy',
			'repo': 'PlasmaPy',
			'branch': 'master',
			'binderhub_url': 'https://mybinder.org',
			'dependencies': ['../binder/requirements.txt'],
			'notebooks_dir': 'plasmapy/examples',
		}
	}

and add this fragment of ``sphinx_gallery.binder`` code with a modification into Sphinx's ``conf.py`` file:

.. code:: python
    
    # Patch sphinx_gallery.binder.gen_binder_rst so as to point to .py file in repository
    import sphinx_gallery.binder
    def patched_gen_binder_rst(fpath, binder_conf, gallery_conf):
    	"""Generate the RST + link for the Binder badge.
    	...
    	"""
    	binder_conf = sphinx_gallery.binder.check_binder_conf(binder_conf)
    	binder_url = sphinx_gallery.binder.gen_binder_url(fpath, binder_conf, gallery_conf)
    
    	# I added the line below:
    	binder_url = binder_url.replace(gallery_conf['gallery_dirs'] + os.path.sep, "").replace("ipynb", "py")
    
    	rst = (
    		"\n"
    		"  .. container:: binder-badge\n\n"
    		"    .. image:: https://mybinder.org/badge_logo.svg\n"
    		"      :target: {}\n"
    		"      :width: 150 px\n").format(binder_url)
    	return rst

    # And then we finish our monkeypatching misdeed by redirecting sphinx-gallery to use our function:
    sphinx_gallery.binder.gen_binder_rst = patched_gen_binder_rst


The current gallery is located `here <http://docs.plasmapy.org/en/latest/auto_examples/index.html>`_, and an example link is https://mybinder.org/v2/gh/PlasmaPy/PlasmaPy/master?filepath=plasmapy/examples/particle_stepper.py - and you should instantly see it points to the right spot!

Obviously, it would be better to implement such link customization in sphinx-gallery itself somehow, but it's up to their maintainers to decide whether this kind of combo usage with Jupytext is in scope for their project. For now, the monkeypatch solution works decently. I'll try to update this post if that comes about.

Update - requirements
=====================

`@jdkent on GitHub <https://github.com/PlasmaPy/PlasmaPy/pull/689>`_ suggests that if the above doesn't work for you, you should make sure the Sphinx version you're using is 2 or newer.
