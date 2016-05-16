# asterix
Manage python components startup quickly and efficiently

[![Code Climate](https://codeclimate.com/github/hkupty/asterix/badges/gpa.svg)](https://codeclimate.com/github/hkupty/asterix)
[![PyPI version](https://badge.fury.io/py/asterix.svg)](https://badge.fury.io/py/asterix)

## What is asterix

Describe the initialization of your application and let asterix manage the
startup for you. It will ensure that the correct dependencies are started
in order, so you don't need any dirty hacks to have your initialization flow.

Also, it allows you to build separate stacks for test/dev/production and even
for web/batch applications, loading just what you need.

## How to use

Simply describe what are the components you need to have your application up
and running, what are their dependencies and how to start them.

Also, asterix allows you to run hooks after components are started.

Lastly, asterix will bind the components reference into an object, so you can
properly recover them later. You can reference one of the started components
or pass an object into `"bind_to"`.

```python
def register_blueprint(app):
    from .api_v1 import my_api
    app.register_blueprint(my_api, url_prefix='/my/api')

components = {
    "components": {
        "config": (set(), get_config),
        "app": ({"config", }, create_app),
        "marshmallow": ({"app", }, lambda app: Marshmallow(app)),
        "db": ({"config", }, start_db)
    },
    "hooks": {
        "app" :[
          register_blueprint
        ],
    },
    "bind_to": "app"
}
```

## The `components`
The `components` section defines your components. Whatever you need to have
up and running while your application is on. Databases, messaging, caches or
even smaller pieces of code that require to be started during initialization
process.

You just need to supply a tuple with the set of dependencies this component
has and how to start it.

Everything in asterix is name bound, so once you define `app` as a component
name, it will be passed to functions who require it with the same name.
(i.e. the Marshmallow lambda above)

## The `hooks`

You can also add hooks to initialized components (i.e. post processing) to
allow side effects to happen after component has started.

This will be run immediately after it has started.

## The `bind_to`

Asterix will keep track of the components by binding it to an object.

After initalization process, you can
`asterix.get_component("component", bound_object)` and get the component
you want.

This is important so you won't have `from app import component` on your code,
which allows better testing as components are not import bound anymore.


## Credits
Although I did it myself, it is completely based on
[system](https://github.com/danielsz/system).
