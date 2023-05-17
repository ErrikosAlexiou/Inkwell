import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'dart:io' show Platform;
import 'webLib/webmain.dart';
import 'winLib/winmain.dart';
import 'androidLib/androidmain.dart';
import 'iosLib/ioslib.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    if (kIsWeb) {
      return const MaterialApp(
        home: webApp(),
      );
    } else if (Platform.isWindows) {
      return const MaterialApp(
        home: WindowsApp(),
      );
    } else if (Platform.isAndroid) {
      return const MaterialApp(
        home: AndroidApp(),
      );
      // } else if (Platform.isIOS) {
      //   return const MaterialApp(
      //     home: iOSApp(),
      // ); iOS testing not implimented until i can emulate ios on windows
    } else {
      return const MaterialApp(
        home: notsureApp(),
      );
    }
  }
}

class notsureApp extends StatelessWidget {
  const notsureApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Not Sure App'),
      ),
      body: const Center(
        child: Text('This is the Not Sure version of the app'),
      ),
    );
  }
}
