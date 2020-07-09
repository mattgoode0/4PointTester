import QtQuick 2.0
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.12


ApplicationWindow {
    id: page
    width: 600
    height: 400
    visible: true
    title: "Keithley Test App"

    Grid {
        id: grid
        anchors.fill: parent


        RowLayout {
            id: topRow
            width: 600
            height: 270
            spacing: 10
            transformOrigin: Item.Center

            ColumnLayout {
                id: leftColumn
                x: 20
                y: 10
                width: 200
                height: 400
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                transformOrigin: Item.Right


                TextField {
                    id: sample_name
                    placeholderText: qsTr("Sample Name")
                }

                TextField {
                    id: start_value
                    placeholderText: qsTr("Start Value")
                }

                TextField {
                    id: end_value
                    placeholderText: qsTr("End Value")
                }

                TextField {
                    id: num_steps
                    placeholderText: qsTr("Number of Steps")
                }

                TextField {
                    id: wait_time
                    placeholderText: qsTr("Pause Time")
                }



            }

            Column {
                id: leftmiddlecolumn
                width: 200
                height: 400

                property var sweep_type: ""

                RadioButton {
                    id: linear
                    x: 0
                    text: qsTr("Linear")
                    checked: false
                    onToggled: {
                        leftmiddlecolumn.sweep_type = "LINear"
                    }
                }

                RadioButton {
                    id: log
                    text: qsTr("Log")
                    checked: false
                    onToggled: {
                        leftmiddlecolumn.sweep_type = "LOG"
                    }
                }
            }

            Column {
                id: middleColumn
                x: 300
                y: 40
                width: 200
                height: 400

                property var measrument_units: ""

                RadioButton {
                    id: current
                    x: 0
                    text: qsTr("Current")
                    checked: false
                    onToggled: {
                        middleColumn.measrument_units = "CURRent"
                    }
                }

                RadioButton {
                    id: votlage
                    text: qsTr("Voltage")
                    checked: false
                    onToggled: {
                        middleColumn.measrument_units = "VOLT"
                    }
                }


            }

            Column {
                id: rightColumn
                y: 40
                width: 200
                height: 400

                property var measurment_mode: ""


                RadioButton {
                    id: four_point
                    text: qsTr("4 Point")
                    onToggled: {
                        rightColumn.measurment_mode = "RSENSE ON"
                    }
                }

                RadioButton {
                    id: two_point
                    text: qsTr("2 Point")
                    onToggled: {
                        rightColumn.measurment_mode = "RSENSE OFF"
                    }
                }

            }

        }


    }

    Button {
        id: start
        x: 468
        y: 300
        width: 120
        height: 52
        text: qsTr("Start Test")
        onClicked:{
            status.text = con.start_test(sample_name.text, start_value.text, end_value.text, num_steps.text, wait_time.text,
                           middleColumn.measrument_units , rightColumn.measurment_mode, leftmiddlecolumn.sweep_type)
        }
    }

    Image {
        id: image
        x: 0
        y: 363
        width: 600
        height: 38
        fillMode: Image.PreserveAspectFit
        source: "ISUBanner.png"
    }

    Text {
        id: status
        x: 53
        y: 319
        text: qsTr("")
        font.pixelSize: 15
    }




}

/*##^##
Designer {
    D{i:1;anchors_height:400;anchors_width:492;anchors_x:0;anchors_y:0}
}
##^##*/
