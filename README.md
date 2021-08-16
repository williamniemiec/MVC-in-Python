# MVC in Python
![](https://github.com/williamniemiec/MVC-in-Python/blob/master/media/logo/mvc-in-python_logo.jpg?raw=true)

This project aims to provide an MVC Python framework for you to use in your projects. If you want to see an example of this framework there is a simple and complete example about a database manager. I believe that this example will make understanding easier of how the mechanics of MVC works in Python, in addition to give you a general view of how to make a project with this pattern.

<hr />

## What is MVC?
Briefly, MVC (Model View Controller) is a design pattern widely used in projects because it leaves the project structured in order to facilitate the identification of application modules, understand how it is structured, in addition to facilitating maintenance. It structures the project in three modules:

|Name| Funcion
|------- | -------------- 
|Models | Responsible for business logic
|View | Responsible for the visual part
|Controllers | Responsible for the behavior of the visual part


## How to use this structure in my project?
The [core directory](https://github.com/williamniemiec/MVC-in-Python/blob/master/src/core) contains all classes responsible for MVC operations in Python. If you want to use this structure in your project, you need to know how to use the two classes contained in the core directory: [Core](https://github.com/williamniemiec/MVC-in-Python/blob/master/src/core/Core.py) (responsible for opening controllers) and [Controller](https://github.com/williamniemiec/MVC-in-Python/blob/master/src/core/Controller.py) (responsible for opening views).

### Opening controllers
[Core](https://github.com/williamniemiec/MVC-in-Python/blob/master/src/core/Core.py) class has a method called "openController", which takes the controller name as a parameter (without including "Controller" in its name). It is crucial that when creating your controllers you follow the following nomenclature:
- File name: <i>&lt;NameController&gt;</i>Controller&#46;py
- Class name:  <i>NameController</i>

<b>Note that the controller name must starts with a capital letter</b>
##### Ex - Open <code>src/controllers/HomeController.py</code>
 <pre>
  from core.Core import Core
 
  home = Core.openController("home")
 </pre>

All application controllers must extend the ["Controller" class](https://github.com/williamniemiec/MVC-in-Python/blob/master/src/core/Controller.py), located in <code>src/core/Controller.py</code>. To open a view inside a controller, just call "loadView" method passing the view name as a parameter.

##### Ex - Open <code>src/views/AddView.py</code>
 <pre>
  from core.Controller import Controller
 
  class AddController(Controller):
    def __init__(self):
        self.addView = self.loadView("add")
 </pre>

### Views creation
For creating views you must use the following naming pattern:
- File name: <i>&lt;NameView&gt;</i>View&#46;py
- Class name:  <i>NameView</i>
Furthermore, all view classes must extend [View class](https://github.com/williamniemiec/MVC-in-Python/blob/master/src/views/View.py).

<b>Note that the view name must starts with a capital letter</b>

## Export for personal project
The contents of the [src folder](https://github.com/williamniemiec/MVC-in-Python/blob/master/src) are all you need to apply this pattern to your project.

## Overview of a generic MVC Python framework structure
![](https://github.com/williamniemiec/MVC-in-Python/blob/master/media/uml/uml.png)

## Project organization
The project is in src folder. In it, there are four folders and two files.

### /src
|Name| Type| Function
|------- | --- | ----
| controllers | `Directory`| Contains all application controller classes
| core | `Directory`| Contains the classes responsable for the MVC operations in Python
| models | `Directory`| Contains all application model classes
| views | `Directory`| Contains all application view classes
| config&#46;py | `File`| MVC configuration file (it is important for Core class)
| Main&#46;py | `File`| File responsible for the application start

### /tests
|Name| Type| Function
|------- | --- | ----
| core | `Directory`| Contains all tests related to the Core class


## Example
A simple and complete example of an application using this framework can be obtained from the [example folder](https://github.com/williamniemiec/MVC-in-Python/blob/master/example).
