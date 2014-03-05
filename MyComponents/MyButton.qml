import QtQuick 2.1

// Basically a button:
Rectangle {
    id: root
    width: text.contentWidth + 10
    height: 26
    color: 'lightgrey'
    radius: 5
    
    signal clicked
    property string text
    
    Text {
        id: text
        anchors.centerIn: parent
        text: parent.text
    }
    MouseArea {
        anchors.fill: parent
        onPressed: root.color = 'darkgrey'
        onReleased: root.color = 'lightgrey'
        onClicked: root.clicked()
    }
}