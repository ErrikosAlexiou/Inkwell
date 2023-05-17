import 'package:flutter/material.dart';

class webApp extends StatelessWidget {
  const webApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Web App'),
      ),
      body: const Center(
        child: Text('This is the Web version of the app'),
      ),
    );
  }
}
