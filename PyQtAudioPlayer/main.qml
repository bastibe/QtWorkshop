import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import QtQuick.Dialogs 1.1
import Player 1.0

ApplicationWindow {
    title: "Simple Audio Player: %1".arg(player.filename)
    height: 200
    width: 500
    Player {
        id: player
    }
    ColumnLayout {
        anchors.fill: parent
        RowLayout {
            Button {
                text: "Open File"
                 onClicked: openFile.open()
                 FileDialog {
                     id: openFile
                     nameFilters: ["Sound Files (*.wav *.flac)"]
                     onAccepted: player.filename = fileUrl
                 }
            }
            Button {
                text: player.isPlaying ? "Pause" : "Play"
                enabled: player.filename !== ""
                onClicked: player.isPlaying = !player.isPlaying
            }
        }
        Canvas {
            property variant waveform: player.waveform
            onWaveformChanged: requestPaint()
            implicitWidth: 500
            implicitHeight: 150
            contextType: "2d"
            onPaint: {
                context.save()
                context.fillStyle = "white"
                context.fillRect(0, 0, width, height )
                // draw the waveform (lower half)
                context.fillStyle = "blue"
                context.beginPath()
                context.moveTo(0, height/2)
                for (var idx in waveform) {
                    context.lineTo(idx/waveform.length*width,
                                   -waveform[idx].x*height/2+height/2)
                }
                context.closePath()
                context.fill()
                // draw the waveform (upper half)
                context.beginPath()
                context.moveTo(0, height/2)
                for (var idx in waveform) {
                    context.lineTo(idx/waveform.length*width,
                                   -waveform[idx].y*height/2+height/2)
                }
                context.closePath()
                context.fill()
                context.restore()
            }
            Rectangle {
                property real progress: player.progress/player.length
                color: "red"
                x: parent.width*progress
                width: 1
                y: 0
                height: parent.height
            }
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    player.scrub(mouse.x / width * player.length)
                }
            }
        }
    }
}
