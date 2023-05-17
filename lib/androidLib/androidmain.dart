import 'package:flutter/material.dart';

class AndroidApp extends StatefulWidget {
  const AndroidApp({super.key});

  @override
  State<AndroidApp> createState() => _AndroidAppState();
}

class _AndroidAppState extends State<AndroidApp> {
  int currentPageIndex = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Android App'),
      ),
      body: <Widget>[
        Container(
          color: Colors.red,
          alignment: Alignment.center,
          child: const Text('Page 1'),
        ),
        Container(
          color: Colors.green,
          alignment: Alignment.center,
          child: const Text('Page 2'),
        ),
      ][currentPageIndex],
      bottomNavigationBar: NavigationBar(
        animationDuration: const Duration(milliseconds: 300),
        labelBehavior: NavigationDestinationLabelBehavior.onlyShowSelected,
        onDestinationSelected: (int index) {
          setState(() {
            currentPageIndex = index;
          });
        },
        selectedIndex: currentPageIndex,
        destinations: const <Widget>[
          NavigationDestination(
            selectedIcon: Icon(
              Icons.explore,
              size: 20,
            ),
            icon: Icon(
              Icons.explore,
            ),
            label: 'Explore',
          ),
          NavigationDestination(
            selectedIcon: Icon(
              Icons.commute,
              size: 20,
            ),
            icon: Icon(
              Icons.commute,
            ),
            label: 'Commute',
          ),
        ],
      ),
    );
  }
}
