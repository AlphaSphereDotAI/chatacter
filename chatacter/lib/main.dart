import 'package:flutter/material.dart';
import 'package:appwrite/appwrite.dart';
import 'package:appwrite/models.dart' as models;

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  Client client = Client();
  client = Client()
      .setEndpoint("https://cloud.appwrite.io/v1")
      .setProject("650209298acac4ee1bb6");
  Account account = Account(client);

  runApp(MyForm(
    account: account,
  ));
}

class MyForm extends StatefulWidget {
  final Account account;

  const MyForm({super.key, required this.account});

  @override
  MyFormState createState() {
    return MyFormState();
  }
}

class MyFormState extends State<MyForm> {
  models.User? loggedInUser;
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final TextEditingController nameController = TextEditingController();

  Future<void> login(String email, String password) async {
    await widget.account.createEmailSession(email: email, password: password);
    final user = await widget.account.get();
    setState(() {
      loggedInUser = user;
    });
  }

  Future<void> register(String email, String password, String name) async {
    await widget.account.create(
        userId: ID.unique(), email: email, password: password, name: name);
    await login(email, password);
  }

  Future<void> logout() async {
    await widget.account.deleteSession(sessionId: 'current');
    setState(() {
      loggedInUser = null;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(loggedInUser != null
            ? 'Logged in as ${loggedInUser!.name}'
            : 'Not logged in'),
        const SizedBox(height: 16.0),
        TextField(
          controller: emailController,
          decoration: const InputDecoration(labelText: 'Email'),
        ),
        const SizedBox(height: 16.0),
        TextField(
          controller: passwordController,
          decoration: const InputDecoration(labelText: 'Password'),
          obscureText: true,
        ),
        const SizedBox(height: 16.0),
        TextField(
          controller: nameController,
          decoration: const InputDecoration(labelText: 'Name'),
        ),
        const SizedBox(height: 16.0),
        ElevatedButton(
          onPressed: () {
            login(emailController.text, passwordController.text);
          },
          child: const Text('Login'),
        ),
        ElevatedButton(
          onPressed: () {
            register(emailController.text, passwordController.text,
                nameController.text);
          },
          child: const Text('Register'),
        ),
        ElevatedButton(
          onPressed: () {
            logout();
          },
          child: const Text('Logout'),
        ),
      ],
    );
  }
}
