# SagSag PythonSandbox

(with vscode) best method

## 1. [Install Visual Studio Code](https://code.visualstudio.com/)

## 2. Next, install the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

from the Visual Studio Marketplace. For additional details on installing extensions, see [Extension Marketplace](https://code.visualstudio.com/docs/editor/extension-gallery). The Python extension is named Python and it's published by Microsoft.

# Work with this

## 1. [download git](https://git-scm.com/downloads)

## 2. then... run in terminal

```console
git clone https://github.com/MDLGH48/sagi_demo.git
```

## 3. in terminal

```console
code sagi_demo
```

## 4. open terminal in vscode and create virtual environment [terminal]

```console
python3.7 -m venv sagi_env
```

(or whatever you want to call your environment ...usually called `env`)

## 5. ACTIVATE VIRTUAL ENVIRONMENT! [terminal]

```console
source sagi_env/bin/activate
```

## 6. install packages inside environment [terminal]

```console
pip install -r requirements.txt
```

## 7. run `main.py`

```console
python3 main.py
```

<hr>
<hr>

# ... OR from scratch

## 3. make folder called `sagi_demo` in desktop

- OR open command prompt and `mkdir sagi_demo` in desktop

## 4. open vscode

- and open `sagi_demo` OR cmd `code desktop/sagi_demo`

## 5. open terminal in vscode and create virtual environment [terminal]

```console
python3.7 -m venv sagi_env
```

(or whatever you want to call your environment ...usually called `env`)

## ACTIVATE VIRTUAL ENVIRONMENT! [terminal]

```console
source sagi_env/bin/activate
```

## install packages [terminal]

```console
pip install numpy opencv-python
```

### read documentation

[opencv docs fast tutorial](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html)

[numpy docs fast tutorial](https://numpy.org/devdocs/user/quickstart.html#an-example)

## make a python file IN the current working directory (`sagi_file.py` OR `main.py` or whatever)

```Python
import numpy as np
import cv2


def numpy_test(x):
    rand_num = np.random.randint(x)
    return f"numpy test... your random number is = {rand_num}"


def cv2_test():
    test_img = cv2.imread('test_image.png', 0)
    cv2.imshow('test_image_window', test_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("open cv works")


if __name__ == "__main__":
    print(numpy_test(3))
    cv2_test()
```

## 7. run your file

```console
python3 sagi_file.py
```
