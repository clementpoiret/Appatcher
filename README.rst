====================
Welcome to Appatcher
====================

Appatcher is a retro(keygen)-inspired linux app intended to automatically decompile, patch, obfuscate and recompile Android applications.

The application is in the public domain. I do not take any responsibility for any damage or illegal use of this software. Use it at your own risk, and only for legal purposes.

The patch has to be a valid diff file acting on smali (or assets) files.

.. image:: https://raw.githubusercontent.com/clementpoiret/Appatcher/main/screenshot.png
  :width: 800
  :alt: Example: using Appatcher to patch an app


Patch sample
------------

Please find attached a sample patch file for a FAKE APP. Any resemblance to real apps is purely coincidental and is not intended.

.. code-block:: diff

    diff -Naur ./.tmpbak/decompiled/res/values/strings.xml ./.tmp/decompiled/res/values/strings.xml
    --- ./.tmpbak/decompiled/res/values/strings.xml	2021-07-26 11:28:35.000000000 +0200
    +++ ./res/values/strings.xml	2021-07-26 11:43:10.058160096 +0200
    @@ -278,7 +278,7 @@
        <string name="nav_menu_payment">Payment</string>
        <string name="nav_menu_settings">Account</string>
        <string name="nav_menu_terms">Terms</string>
    -    <string name="nav_menu_version">Version %1$s_%2$d</string>
    +    <string name="nav_menu_version">v%1$s build %2$d patched</string>
        <string name="nav_menu_visualizations">Debug</string>
        <string name="nav_menu_webview_debugging">debugging</string>
        <string name="nav_practice">Practice</string>
    diff -Naur ./.tmpbak/decompiled/smali/c/a/c/c/a.smali ./.tmp/decompiled/smali/c/a/c/c/a.smali
    --- ./.tmpbak/decompiled/smali/c/a/c/c/a.smali	2021-07-26 11:28:37.000000000 +0200
    +++ ./smali/c/a/c/c/a.smali	2021-07-26 11:32:50.082134302 +0200
    @@ -126,6 +126,8 @@
        iput-object p3, p0, Lc/a/c/c/a;->e:Ljava/lang/String;
    
        .line 5
    +    const/4 p4, 0x1
    +    
        iput-boolean p4, p1, Lc/a/c/c/a;->f:Z
    
        .line 6
    diff -Naur ./.tmpbak/decompiled/smali/org/testapp/android/api/responses/Responses.smali ./.tmp/decompiled/smali/org/testapp/android/api/responses/Responses.smali
    --- ./.tmpbak/decompiled/smali/org/testapp/android/api/responses/Responses.smali	2021-07-26 11:28:41.000000000 +0200
    +++ ./smali/org/testapp/android/api/responses/Responses.smali	2021-07-26 11:31:30.190130978 +0200
    @@ -31,7 +31,7 @@
    
        const/4 v0, 0x0
    
    -    const/4 v1, 0x0
    +    const/4 v1, 0x1
    
        .line 1
        invoke-direct {p0}, Ljava/lang/Object;-><init>()V
    diff -Naur ./.tmpbak/decompiled/smali/org/testapp/android/api/responses/User.smali ./.tmp/decompiled/smali/org/testapp/android/api/responses/User.smali
    --- ./.tmpbak/decompiled/smali/org/testapp/android/api/responses/User.smali	2021-07-26 11:28:41.000000000 +0200
    +++ ./smali/org/testapp/android/api/responses/User.smali	2021-07-26 11:33:49.302136766 +0200
    @@ -113,7 +113,7 @@
        .line 5
        iput-object v0, p0, Lorg/testapp/android/api/responses/User;->pseudo:Ljava/lang/String;
    
    -    const/4 v1, 0x0
    +    const/4 v1, 0x1
    
        .line 6
        iput-boolean v1, p0, Lorg/testapp/android/api/responses/User;->hasProSubscription:Z


