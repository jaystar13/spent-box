import 'package:flutter/material.dart';

class MonthlyDetailPage extends StatelessWidget {
  final int year;
  final int month;

  const MonthlyDetailPage({super.key, required this.year, required this.month});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('$year년 $month월 상세 내역')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              '$year년 $month월 요약',
              style: Theme.of(context).textTheme.titleLarge,
            ),
            SizedBox(height: 16),
            Card(
              elevation: 2,
              child: ListTile(
                leading: Icon(Icons.arrow_upward, color: Colors.green),
                title: Text('수입'),
                trailing: Text('₩1,000,000'),
              ),
            ),
            Card(
              elevation: 2,
              child: ListTile(
                leading: Icon(Icons.arrow_downward, color: Colors.red),
                title: Text('지출'),
                trailing: Text('₩800,000'),
              ),
            ),
            SizedBox(height: 24),
            Text('카테고리별 지출', style: Theme.of(context).textTheme.titleMedium),
            SizedBox(height: 8),
            Expanded(
              child: ListView(
                children: [
                  ListTile(
                    leading: Icon(Icons.fastfood),
                    title: Text('식비'),
                    trailing: Text('₩300,000'),
                  ),
                  ListTile(
                    leading: Icon(Icons.shopping_cart),
                    title: Text('쇼핑'),
                    trailing: Text('₩200,000'),
                  ),
                  ListTile(
                    leading: Icon(Icons.house),
                    title: Text('주거'),
                    trailing: Text('₩150,000'),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: Padding(
        padding: const EdgeInsets.fromLTRB(16, 8, 16, 30),
        child: ElevatedButton(
          onPressed: () {
            // 업로드 화면 이동 or 파일 선택 로직
            print('소비내역 업로드 버튼 눌림');
          },
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.blue, // 배경 파란색
            foregroundColor: Colors.white, // 글자 흰색
            padding: const EdgeInsets.symmetric(vertical: 16),
            textStyle: const TextStyle(fontSize: 16),
          ),
          child: const Text('소비내역 업로드'),
        ),
      ),
    );
  }
}
