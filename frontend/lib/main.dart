import 'package:flutter/material.dart';
import 'package:frontend/pages/monthly_detail_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Spent Box',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const MyHomePage(title: 'Spent Box'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int selectedYear = 2025;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text('${widget.title} - $selectedYear'),
        actions: [
          PopupMenuButton(
            icon: Icon(Icons.calendar_today),
            itemBuilder: (context) => List.generate(10, (i) {
              int year = 2025 - i;
              return PopupMenuItem(value: year, child: Text('$year년'));
            }),
            onSelected: (year) {
              setState(() {
                selectedYear = year;
              });
            },
          ),
        ],
      ),
      body: SafeArea(
        bottom: true,
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 12.0),
          child: CustomScrollView(
            slivers: [
              SliverToBoxAdapter(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      '총 지출내역: 7,800,500 원',
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    SizedBox(height: 16),
                  ],
                ),
              ),
              SliverPadding(
                padding: EdgeInsets.only(bottom: 32),
                sliver: SliverGrid(
                  delegate: SliverChildBuilderDelegate((context, index) {
                    int month = index + 1;
                    return InkWell(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (_) => MonthlyDetailPage(
                              month: month,
                              year: selectedYear,
                            ),
                          ),
                        );
                      },
                      borderRadius: BorderRadius.circular(12),
                      child: Container(
                        decoration: BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.circular(12),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.black12,
                              blurRadius: 4,
                              offset: Offset(0, 2),
                            ),
                          ],
                        ),
                        padding: const EdgeInsets.all(12),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            FittedBox(
                              fit: BoxFit.scaleDown,
                              child: Text(
                                '$month월',
                                style: TextStyle(fontWeight: FontWeight.bold),
                              ),
                            ),

                            SizedBox(height: 8),
                            FittedBox(
                              fit: BoxFit.scaleDown,
                              child: Text('지출: 800,000원'),
                            ),
                            FittedBox(
                              fit: BoxFit.scaleDown,
                              child: Text('수입: 1,000,000원'),
                            ),
                          ],
                        ),
                      ),
                    );
                  }, childCount: 12),
                  gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 3,
                    crossAxisSpacing: 12,
                    mainAxisSpacing: 12,
                    childAspectRatio: 1.2,
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
