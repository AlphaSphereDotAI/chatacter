import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:url_launcher/link.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'alpha-AI Team',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        scaffoldBackgroundColor: const Color(0xFF000000),
      ),
      home: Scaffold(
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              AnimatedTextKit(
                animatedTexts: [
                  TypewriterAnimatedText(
                    'alpha-AI Team',
                    textStyle: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                      fontSize: (MediaQuery.of(context).size.width * 0.1 <
                              MediaQuery.of(context).size.height * 0.1)
                          ? MediaQuery.of(context).size.width * 0.1
                          : MediaQuery.of(context).size.height * 0.1,
                      fontFamily: GoogleFonts.jetBrainsMono().fontFamily,
                    ),
                    speed: const Duration(milliseconds: 100),
                  ),
                ],
                repeatForever: false,
                isRepeatingAnimation: false,
              ),
              AnimatedTextKit(
                animatedTexts: [
                  TypewriterAnimatedText(
                    'Graduation Project at Faculty of Computers and Artificial Intelligence, Cairo University',
                    textStyle: TextStyle(
                      color: Colors.white,
                      fontSize: (MediaQuery.of(context).size.width * 0.03 <
                              MediaQuery.of(context).size.height * 0.03)
                          ? MediaQuery.of(context).size.width * 0.03
                          : MediaQuery.of(context).size.height * 0.03,
                      fontFamily: GoogleFonts.jetBrainsMono().fontFamily,
                    ),
                    speed: const Duration(milliseconds: 50),
                  ),
                ],
                repeatForever: false,
                isRepeatingAnimation: false,
              ),
              const SizedBox(
                height: 30,
              ),
              AnimatedTextKit(
                animatedTexts: [
                  TypewriterAnimatedText(
                    'Team Members:\n• Mohamed Hisham Abdelzaher\n• Yousef Mohamed AbdEl-Hay\n• Abdelrahman Mostafa Mohamed\n• Beshoy Madhat Sadeq\n• Rina Khaled Ahmed\n• Shereen Ashraf Ahmed',
                    textStyle: TextStyle(
                      color: Colors.white,
                      fontSize: (MediaQuery.of(context).size.width * 0.03 <
                              MediaQuery.of(context).size.height * 0.03)
                          ? MediaQuery.of(context).size.width * 0.03
                          : MediaQuery.of(context).size.height * 0.03,
                      fontFamily: GoogleFonts.jetBrainsMono().fontFamily,
                    ),
                    speed: const Duration(milliseconds: 50),
                  ),
                ],
                repeatForever: false,
                isRepeatingAnimation: false,
              ),
              const SizedBox(
                height: 30,
              ),
              Link(
                target: LinkTarget.blank,
                uri: Uri.parse('MAILTO:alpha-AI@googlegroups.com'),
                builder: (context, followLink) => OutlinedButton(
                  onPressed: followLink,
                  child: AnimatedTextKit(
                    onTap: followLink,
                    animatedTexts: [
                      TypewriterAnimatedText(
                        'alpha-AI@googlegroups.com',
                        textStyle: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                          fontSize: (MediaQuery.of(context).size.width * 0.03 <
                                  MediaQuery.of(context).size.height * 0.03)
                              ? MediaQuery.of(context).size.width * 0.03
                              : MediaQuery.of(context).size.height * 0.03,
                          fontFamily: GoogleFonts.jetBrainsMono().fontFamily,
                        ),
                        speed: const Duration(milliseconds: 100),
                      ),
                    ],
                    repeatForever: false,
                    isRepeatingAnimation: false,
                  ),
                ),
              ),
              const SizedBox(
                height: 30,
              ),
              Link(
                target: LinkTarget.blank,
                uri: Uri.parse('https://github.com/MH0386/graduation_project'),
                builder: (context, followLink) => OutlinedButton(
                  onPressed: followLink,
                  child: AnimatedTextKit(
                    onTap: followLink,
                    animatedTexts: [
                      TypewriterAnimatedText(
                        'Our GitHub Repository',
                        textStyle: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                          fontSize: 30,
                          fontFamily: GoogleFonts.jetBrainsMono().fontFamily,
                        ),
                        speed: const Duration(milliseconds: 200),
                      ),
                    ],
                    repeatForever: false,
                    isRepeatingAnimation: false,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
