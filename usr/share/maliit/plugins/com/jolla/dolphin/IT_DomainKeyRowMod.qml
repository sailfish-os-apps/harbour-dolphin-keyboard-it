import QtQuick 2.0
import com.jolla.keyboard 1.0

KeyboardRow {
    splitIndex: 2

    IT_DomainKeyMod {
        id: dk1
        caption: "https://"
        text: "https://"
        anchors.left: parent.left
    }
    IT_DomainKeyMod {
        caption: ".com"
        text: ".com"
        anchors.left: dk1.right
    }
    IT_DomainKeyMod {
        caption: ".it"
        text: ".it"
        anchors.right: dk4.left
    }
    IT_DomainKeyMod {
        id: dk4
        caption: ".org"
        text: ".org"
        anchors.right: parent.right
    }

}
