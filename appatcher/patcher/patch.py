import os
import subprocess
from pathlib import Path

import patch as patch_


def sanity_checks(apk, patch):
    if not apk.exists():
        return 0, "APK not found"

    if not patch.exists():
        return 0, "Patch not found"

    return 1, "OK"


def patch(patch_file, root):
    pset = patch_.fromfile(patch_file)
    pset.apply(root=root)


def decompile(apk, dst):
    apktoold = subprocess.Popen([
        "java",
        "-jar",
        "appatcher/thirdparty/apktool/apktool_2.5.0.jar",
        "d",
        apk,
        "-o",
        dst,
    ],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)

    return apktoold.communicate()


def obfuscate(dst):
    smob = subprocess.Popen(
        ["./appatcher/thirdparty/smob/smob", "-p", "-i", dst],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)

    return smob.communicate()


def recompile(src, apk):
    apktoolb = subprocess.Popen([
        "java",
        "-jar",
        "appatcher/thirdparty/apktool/apktool_2.5.0.jar",
        "b",
        src,
        "-o",
        apk,
    ],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)

    return apktoolb.communicate()


def sign(apk, dst):
    signer = subprocess.Popen([
        "java",
        "-jar",
        "appatcher/thirdparty/uas/uber-apk-signer-1.2.1.jar",
        "-a",
        apk,
        "-o",
        dst,
    ],
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              text=True)

    return signer.communicate()
