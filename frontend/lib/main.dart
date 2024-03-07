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
        // theme: ThemeData(
        //   colorScheme: const ColorScheme(
        //     primary: Colors.black,
        //     secondary: Colors.red,
        //     surface: Colors.white,
        //     background: Color.fromARGB(255, 255, 255, 255),
        //     error: Colors.red,
        //     onPrimary: Colors.white,
        //     onSecondary: Colors.white,
        //     onSurface: Colors.black,
        //     onBackground: Colors.black,
        //     onError: Colors.white,
        //     brightness: Brightness.light,
        //   ),
        // ),
        initialRoute: '/',
        routes: {
          '/': (context) => const Home(),
          '/chat': (context) => const Chat(),
        });
  }
}
