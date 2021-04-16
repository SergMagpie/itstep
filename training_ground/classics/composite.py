from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    Базовый класс Component объявляет общие операции как для простых, так и для
    сложных объекты композиции
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        При желании базовый компонент может объявить интерфейс для установки 
        и доступа к родительскому элементу компонента в древовидной структуре. 
        Он также может предоставить некоторую реализацию по умолчанию для этих методов.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    В некоторых случаях было бы полезно определить операции управления дочерними 
    элементами прямо в базовом классе Component. Таким образом, вам не нужно 
    будет предоставлять клиентскому коду какие-либо конкретные классы 
    компонентов, даже во время сборки дерева объектов. Обратной стороной 
    является то, что эти методы будут пустыми для компонентов конечного уровня.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        Вы можете предоставить метод, который позволяет клиентскому коду выяснить, 
        может ли компонент иметь потомков.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        Базовый Компонент может реализовать какое-то поведение по умолчанию 
        или оставить его для конкретных классов (объявив метод, 
        содержащий поведение, как «абстрактный»).
        """

        pass


class Leaf(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    Класс Leaf представляет конечные объекты композиции. У листа не может быть детей.
    Обычно фактическую работу выполняют объекты Leaf, 
    тогда как объекты Composite делегируют свои полномочия только своим субкомпонентам.
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    Класс Composite представляет сложные компоненты, 
    у которых могут быть дочерние элементы. Обычно объекты Composite 
    делегируют реальную работу своим дочерним элементам, 
    а затем «суммируют» результат.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    Составной объект может добавлять или удалять другие компоненты 
    (как простые, так и сложные) в свой дочерний список или из него.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        Composite определенным образом выполняет свою основную логику. 
        Он рекурсивно проходит через всех своих дочерних элементов, 
        собирая и суммируя их результаты. Поскольку дочерние элементы 
        композита передают эти вызовы своим дочерним элементам и т. д., 
        В результате выполняется обход всего дерева объектов.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    Клиентский код работает со всеми компонентами через базовый интерфейс.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple or
    complex, without depending on their concrete classes.
    Благодаря тому, что операции управления потомками объявлены 
    в базовом классе Component, клиентский код может работать с любым компонентом, 
    простым или сложным, вне зависимости от их конкретных классов.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    # Таким образом, клиентский код может поддерживать простые листовые компоненты ...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    # ... а также сложные композиты.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
