import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:chatacter/Pages/chat.dart';
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        elevation: 50,
        leading: IconButton(
          onPressed: () => print('Menu button pressed'),
          icon: Icon(Icons.menu, color: Theme.of(context).colorScheme.primary),
        ),
        title: const Text('Chatacter Demo'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            AnimatedTextKit(
              isRepeatingAnimation: false,
              animatedTexts: [
                TypewriterAnimatedText(
                  'Welcome to Chatacter Demo',
                  textAlign: TextAlign.center,
                  textStyle: const TextStyle(
                    fontWeight: FontWeight.w900,
                    fontSize: 50,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 20),
            AnimatedTextKit(
              isRepeatingAnimation: false,
              animatedTexts: [
                TypewriterAnimatedText(
                  'This is a chatbot app\nClick the button below to start chatting',
                  textAlign: TextAlign.center,
                  textStyle: const TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 30,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 40),
            ElevatedButton(
              onPressed: () {
                print('Button pressed');
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const Chat()),
                );
              },
              style: const ButtonStyle(
                alignment: Alignment.center,
                maximumSize: MaterialStatePropertyAll(
                  Size(400, 50),
                ),
              ),
              child: const Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    Icons.chat_bubble_outline_outlined,
                  ),
                  SizedBox(width: 20),
                  Text('Chat with Napoleon Bonaparte'),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
