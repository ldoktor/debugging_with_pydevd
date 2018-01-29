Introduction
============

* Topic
    * Workshop about debugging python code in Eclipse with pydevd
* Lukáš Doktor
    * happy Red Hatter
    * virt-team
    * Avocado/Avocado-vt maintainer
* final.qcow2 contains:
    * Fedora 27, somehow up-to-date
    * users: test, root
    * password: heslo
    * password-less sudo
    * win+r => run terminal
    * win+e => toggle full-screen
    * win+a => 1st desktop
    * win+b => 2nd desktop


Overview
========

* Install and setup Eclipse with pydev
* Examples:
    * In Eclipse - demonstrate in-eclipse execution
    * From system - use ``vim`` to set breakpoints
    * Real-world - complex projects and cross-arch remote execution
* Challenge
* Summary


Eclipse
=======

Install Eclipse
---------------

* https://www.eclipse.org/
* download
* extract
* run "./eclipse-inst"
* follow the guide (I usually go with C/C++)
* launch it
* pick a suitable workspace
    * new projects are created there
    * you can still import existing location so the workspace path is not that
      important (anyway it has to exist and always will be created on start)
    * personally I use 3 workspace locations for 3 different usages (feel free
      to ask for details)


Install Pydev
-------------

* Help->Install New Software
* Add...
* `pydev`/`http://www.pydev.org/updates`
* checkbox PyDev, next, next, next...
* Icon "Open perspective"->PyDev


Setup Workspace
---------------

* New
* PyDev Project
* Name => test1
* "Configure the interpreter" => Auto config; Next; Finish
* PyDev Package Explorer
* There you see all projects in your Workspace (even when the files are on
  a different location)
* Right-click on $project_name (test1)
* New->File
* File name: "foo.py"
* Create Hello World
* Run (Python Run)


Customize Apperance
-------------------

* Move the windows to not occupy all space
* Ideally clone the window and move it so I can see it twice (somehow can't do
  it now, but I can show it in my working Eclipse)
* Window->New Window
* Open the same source in it (to have some content)
* Move the new window to 2nd screen
* Change perspective to "Debug"
* Setup better layout (note I'm used to portrait mode)


Customize Pydev
---------------

* Add some pydev/pep8 issues
* Window->Preferences
* Pydev->Editor->Code Analysis:
    * pycodestyle.py (pep8) => Warning
    * Use system interpreter
* Apply&close; modify sources and see the additional messages
* ctrl+shift+f => auto-format
* ctrl+shift+o => organize imports
* Preferences; PyDev->Editor->Overview Ruler Minimap
    => Untick "Show in minimap?"
    => tick "Show horizontal scrollbar?"
    => tick "Show overview items in overview ruler?"
* Preferences; PyDev->Editor
    => in "Apperance color options" select "Unicode" & set color #C9802B
    => in "Apperance color options" select "Bytes" & set color #00AA00
* Preferences; PyDev->Editor->Code Style->Code Formatter
    => Tick "Use autopep8.py for code formatting"
* Preferences; PyDev->Editor->Code Style->Docstrings
    => set "Quotation mark (\")"
* Preferences; General->Editors->Text Editors
    => set "Undo history size" = 2000
    => tick "Show print margin"
* Preferences; General->Workspace->Local History
    => set "Days to keep files" = 70
    => set "Maximum entries per file" = 500
    => set "Maximum file size" = 10
* Show local history
    - right click in sources -> team -> show local history


Examples
========

In Eclipse
----------

.. note:: Don't look at the ``black_box.py.missing`` and try whether the
          provided ``black_box.pyc`` is importable. If not, rename the
          ``black_box.py.missing`` to ``black_box.py`` and compile it
          using your python ``python -m py_compile black_box.py``,
          then rename it back. That way ``black_box`` should be importable
          but you won't see sources in debugger (to really immitate black
          box).

* move ``Stažené/examples_in_eclipse`` into ``$workspace`` and look at "Project Explorer"
    => see, it's not automatically added
* new->project->general->
    - set the name to the same location
* Alternatively if you import git repos (what I usually do but I stripped the ".git"):
    => File->import...->General->Git
    => Existing local repository
    => Add..
    => Browse -> to the workspace/examples dir & tick the "examples/.git"
    => Next
    => Import as general project (used to be recommended)
    => Next; Finish
* Right-click on the project
    =>PyDev=>Set as PyDev Project
    =>PyDev=>Set as SOURCE folder

* 01_hello_world.py
    - run it via Eclipse
    - debug it via Eclipse and change the "greetings" to "Hello Devconf"

* 02_loop.py
    - add breakpoints, use F8

* 03_import/import.py
    - add breakpoint before `import` and show the process

* 04_threading.py
    - a - show how to step different threads
    - b - show how locking solves the issue, but how about starving?
    - c - show how to force-go into situation that usually does not happen


Vim+Eclipse
-----------

.. note:: To be able to ``import pydevd`` you need to have ``pydevd`` (not
          just ``pydev``) installed. You can either add the Eclipse one
          in your PYTHONPATH, or you can simply get it from pip by
          ``pip install pydevd``.

* 05_stdout_stderr.py
    - run it with "import pydevd; pydevd.settrace("127.0.0.1")"
    - ctrl+f2
    - Disable firewall on 5678
        * "firewall-cmd --zone public --add-port=5678/tcp"
    - Show how to enable server (and show what happens without running it)
    - let someone from the audience run it with my IP address and show
      their "hostname"
        * import subprocess; print(subprocess.check_output("hostname", shell=True)); print(subprocess.check_output("ifconfig"))

* 06_client_server
    - run a, show why it fails
    - run b, show why it work and step through various types


Real-world (PP)
---------------

.. note:: Here real-world example where in Eclipse debugging significantly
          helped to pin-point and fix the actual issue. There is no simple
          way of expressing it in short in text form so simply find some
          complex project, crash it and walk through to see what is going
          on.

.. note:: The (PP) => product placement is here because I used
          Avocado/Avocado-vt, to demonstrate real-world examples. Feel free
          to check them out here http://avocado-framework.github.io/
          resp. https://github.com/avocado-framework/avocado-vt as they
          might be useful to you.


Challange
=========

.. note:: Here three completely different issues (but sort of similar to
          real-world demonstration) were described for people to get
          their hands dirty trying to fix the issues.

Summary
=======

* Eclipse is nice, tool suitable for debugging, complex code refactoring,
  but sometimes unnecessary. My recommendation is to use ``vim`` to develop
  code, ``print`` to debug basic issues or issues in well known code and
  only use Eclipse to interact with complex issues, remote execution or
  simply to learn about unknown parts of the code. Anyway it's your choice...
