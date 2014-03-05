from PyQt5 import QtCore

def autoProperty(type_, name, readonly=False):
    """Create a Qt/Python property.

    This creates a property that works in both Python and Qt. It acts
    just like a regular Python property, but notifies Qt of every
    update as well. Works only in QObject derived classes

    Attributes:
    type_: The type of the property. This is necessary for Qt.
    name:  The name of the property. This is necessary for Qt.
    readonly: Whether a writer should be created for the property.

    Returns:
    signal:    The Qt signal. Use this to register for updates on the
               property. It must be called name_changed.
    property_: The Python/Qt property. This works just like a regular
               Python property, but notifies Qt of changes, too.

    Usage:
    class Foo(QObject):
        prop_changed, prop = autoProperty(str, 'prop')

    """

    signal = QtCore.pyqtSignal(type_, name=name+'_changed')
    def reader(self):
        return getattr(self, '_'+name)
    def writer(self, value):
        old_value = getattr(self, '_'+name)
        if old_value != value:
            setattr(self, '_'+name, value)
            getattr(self, name+'_changed').emit(value)
    if readonly:
        writer = None
    property_ = QtCore.pyqtProperty(type_, fget=reader, fset=writer, notify=signal)
    return signal, property_
