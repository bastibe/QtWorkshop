import QtQuick 2.1

// Basically a slider:
Rectangle {
    id: groove
    width: 108
    height: 26
    color: 'lightgrey'
    radius: 5
    anchors.centerIn: parent
    
    property real value: 0
    property real minimumValue: 0
    property real maximumValue: 100
    onValueChanged: {
        handle.x = (value-minimumValue) / (maximumValue-minimumValue)
                   * (width-handle.width)
    }
    
    Rectangle {
        id: handle
        color: 'darkgrey'
        width: height
        anchors.top: parent.top
        anchors.bottom: parent.bottom
    }
    MouseArea {
        anchors.fill: parent
        drag.target: handle
        drag.axis: Drag.XAxis
        drag.minimumX: 0
        drag.maximumX: groove.width-handle.width
        function updateValue() {
            groove.value = handle.x/(groove.width-handle.width) *
                   (groove.maximumValue-groove.minimumValue) +
                   groove.minimumValue
        }
        // move the handle when you click the groove
        onClicked: {
            if (mouse.x < handle.width/2) {
                handle.x = 0
            } else if (mouse.x > groove.width-handle.width/2) {
                handle.x = groove.width-handle.width
            } else {
                handle.x = mouse.x - handle.width/2
            }
            // update value when moving
            updateValue()
        }
        // update value when moving
        onPositionChanged: updateValue()
    }
}