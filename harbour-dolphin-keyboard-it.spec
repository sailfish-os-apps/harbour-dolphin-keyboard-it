Name:          harbour-dolphin-keyboard-it
Version:       0.2.0
Release:       1
Summary:       Tastiera italiana + emoji colorate per Dolphin keyboard
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires: harbour-dolphin-keyboard >= 1.2-2
Packager: fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
 Tastiera italiana + emoji colorate per Dolphin keyboard.

%files
/usr/share/maliit/plugins/com/jolla/layouts/IT_Xt9Handler.qml
/usr/share/maliit/plugins/com/jolla/layouts/it+.conf
/usr/share/maliit/plugins/com/jolla/layouts/it+.qml
/usr/share/maliit/plugins/com/jolla/dolphin/KeyboardLayout.qml
/usr/share/maliit/plugins/com/jolla/dolphin/IT_DomainKeyRowMod.qml
/usr/share/maliit/plugins/com/jolla/dolphin/IT_DomainKeyMod.qml

%post
systemctl-user restart maliit-server.service

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm /usr/share/maliit/plugins/com/jolla/layouts/IT_Xt9Handler.qml
rm /usr/share/maliit/plugins/com/jolla/layouts/it+.conf
rm /usr/share/maliit/plugins/com/jolla/layouts/it+.qml
rm /usr/share/maliit/plugins/com/jolla/dolphin/IT_DomainKeyRowMod.qml
rm /usr/share/maliit/plugins/com/jolla/dolphin/IT_DomainKeyMod.qml
systemctl-user restart maliit-server.service
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Aggiornamento"
systemctl-user restart maliit-server.service
fi
fi

%changelog
* Tue Sep 13 2016 0.2.0
- Added domain keys.

* Thu Nov 5 2015 0.1
- Fix for caps lock.

* Mon Nov 2 2015 0.1
- First build.
