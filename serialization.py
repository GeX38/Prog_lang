from enum import Enum
import json


class Alignment(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Widget():

    def __init__(self, parent=None):
        self.parent = parent
        self.children = []
        if self.parent is not None:
            self.parent.add_child(self)

    def add_child(self, child: "Widget"):
        self.children.append(child)

    def to_dict(self):
        return {
            "class": self.__class__.__name__,
            "children": [child.to_dict() for child in self.children] if self.children else [],
            **self.additional_properties()
        }

    def additional_properties(self):
        return {}

    @classmethod
    def from_dict(cls, data):
        instance = cls()
        for child_data in data.get("children", []):
            child_instance = Widget.from_dict(child_data)
            instance.add_child(child_instance)
        return instance

    def __str__(self):
        return f"{self.__class__.__name__}{self.children}"

    def __repr__(self):
        return str(self)


class MainWindow(Widget):

    def __init__(self, title: str):
        super().__init__()
        self.title = title

    def additional_properties(self):
        return {"title": self.title}


class Layout(Widget):

    def __init__(self, parent, alignment: Alignment):
        super().__init__(parent)
        self.alignment = alignment

    def additional_properties(self):
        return {"alignment": self.alignment.name}


class LineEdit(Widget):

    def __init__(self, parent, max_length: int = 10):
        super().__init__(parent)
        self.max_length = max_length

    def additional_properties(self):
        return {"max_length": self.max_length}


class ComboBox(Widget):

    def __init__(self, parent, items):
        super().__init__(parent)
        self.items = items

    def additional_properties(self):
        return {"items": self.items}


app = MainWindow("Application")
layout1 = Layout(app, Alignment.HORIZONTAL)
layout2 = Layout(app, Alignment.VERTICAL)

edit1 = LineEdit(layout1, 20)
edit2 = LineEdit(layout1, 30)

box1 = ComboBox(layout2, [1, 2, 3, 4])
box2 = ComboBox(layout2, ["a", "b", "c"])

print(app)

json_data = json.dumps(app.to_dict(), indent=2)
print(json_data)

new_data = json.loads(json_data)
new_app = Widget.from_dict(new_data)

print(new_app)
