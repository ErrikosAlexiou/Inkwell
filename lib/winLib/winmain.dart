import 'package:flutter/material.dart';

class WindowsApp extends StatelessWidget {
  const WindowsApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Windows App'),
      ),
      body: const Center(
        child: Text('This is the Windows version of the app'),
      ),
    );
  }
}
