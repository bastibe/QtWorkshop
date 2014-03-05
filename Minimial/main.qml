import QtQuick 2.2
import QtQuick.Controls 1.1
import Backend 1.0

ApplicationWindow {
    title: qsTr("Window Title")
    Counter {
        id: counter
    }
    MyButton {
        anchors.centerIn: parent
        text: "Click Me! (%1)".arg(counter.value)
        onClicked: counter.increment()
    }
}
