

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

                           Split  APKs  Packer

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


A simple and fast tool to transform Android App Bundles into single Android Packages.

[HOW IT WORKS]
SAP uses Apktool to decode the resources of the files included in the bundle to be processed.
Then it merges all these files into the base package folder before adjusting and correcting them.
Apktool is used to build the single package, Uber-APK-Signer for zipAlign/sign processes.
SAP doesn't work on dynamic features but configuration modules only

[INFO]
SAP is a portable application ; all files present in its folder are necessary.
For better overall compatibility sap is a 32-bit compiled binary ;)
Two versions are available:
  - for Windows OS ; tested working fine with Wine.
  - for Linux based OS.


[VERSION]
Split APKs Packer v6.9.0
Designed and coded by Kirlif'
Compiled on 16/September/2020


[REQUIREMENTS]
JRE/OpenJDK 1.8 or above ; Java binaries folder present in the system PATH.


[USAGE]
Two ways to create a project:
  - with « Directory » button to choose the folder that contains the split packages to merge.
    SAP will work inside.
  - with « Archive » button to open an app bundle (.apks, .xapk, .zip, .apkm).
    SAP will extract its content in a new folder next to it (archive_name_SAP_Project) and work inside.
SAP check the validity of the bundle then « Select » and « Start » buttons are enabled.
If build succeeded the resulting APK will be found in the « build » folder inside the project directory with the log file.


[FEATURES]
« Select » button allows to customize the project by selecting the wanted split packages:
  - multi-selection and selection of several ranges of items are possible with CTRL key and mouse. 
« Workers » spinner defines the number of concurrent threads to be created for decodings.
  - the maximum number is defined by the number of CPUs.
« Sign » checkbox allows the resulting APK to be zip-aligned and signed:
  - a debug key is used by default. A custom key can be imported thanks to « Keystore » button.
An obfuscated config file is created that contains the parent directory of the last project and the few settings used:
  - it is updated when a custom keystore is imported and when the app is exited.
A log file is created inside the project folder:
  - it is moved into « build » folder at the end of the successful process.
« Start » button will launch the process:
  - split packages decoding.
    During decoding « Start » button is changed to « Cancel » that allows to abandon the project.
  - SAP works on decoded files
  - finally it try to build a single package.
SAP tool allows to merge new split packages with an already SAP repacked APK.


[MANUAL MODE]
If build failed, SAP switch to « Manual Mode »:
  - the « Start » button is changed to « Build » and allows to retry after manual changes.
  - Most of fails are due to not well-formed xml files. Apktool warnings in the log file will help to create fix(es).
The failed project can be abandoned and reopened later.
If the project consists of a single file which is already a SAP repacking, it is automatically decoded.
SAP then switches to « Manual Mode » to allow modding.


[CREDITS]
Connor Tumbleson & Ryszard Wisniewski for Apktool:  https://github.com/iBotPeaches/Apktool
Patrick Favre-Bulle for Uber Apk Signer:  https://github.com/patrickfav/uber-apk-signer
Souradip Mookerjee for unapkm: https://github.com/souramoo/unapkm 
Kay Hayen and Nuitka Organization for Nuitka:  https://github.com/Nuitka/Nuitka
Markus Oberhumer, Laszlo Molnar & John Reiser for UPX:  https://github.com/upx/upx


[CHANGELOG]
- Automatic fonts installation (Windows only - ask for elevation) 
- Fixes, optimizations, ...
- Added new detections and fixes of bundles decoding glitches
- Apktool update
- Android API level 30 support

[CONTACT]
sap_dev@tuta.io

