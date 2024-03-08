import 'package:flutter/material.dart';

import 'Pages/chat.dart';
import 'Pages/home.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Chatacter Demo',
        theme: ThemeData.dark(),
        initialRoute: '/',
        routes: {
          '/': (context) => const Home(),
          '/chat': (context) => const Chat(),
        });
  }
}
