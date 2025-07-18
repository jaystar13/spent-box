import 'package:flutter/material.dart';
import 'package:frontend/pages/expense_upload_page.dart';

class MonthlyDetailPage extends StatefulWidget {
  final int year;
  final int month;

  const MonthlyDetailPage({super.key, required this.year, required this.month});

  @override
  State<MonthlyDetailPage> createState() => _MonthlyDetailPageState();
}

class _MonthlyDetailPageState extends State<MonthlyDetailPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('${widget.year}년 ${widget.month}월'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('내역 요약', style: Theme.of(context).textTheme.titleLarge),
            const SizedBox(height: 16),
            Card(
              elevation: 2,
              child: ListTile(
                leading: const Icon(Icons.arrow_upward, color: Colors.green),
                title: const Text('수입'),
                trailing: const Text('₩1,000,000'),
              ),
            ),
            Card(
              elevation: 2,
              child: ListTile(
                leading: const Icon(Icons.arrow_downward, color: Colors.red),
                title: const Text('지출'),
                trailing: const Text('₩800,000'),
              ),
            ),
            const SizedBox(height: 24),

            // ✅ 카테고리별 지출 (접기/펼치기)
            ExpansionTile(
              initiallyExpanded: true,
              tilePadding: EdgeInsets.zero,
              childrenPadding: EdgeInsets.zero,
              shape: Border.fromBorderSide(BorderSide.none),
              collapsedShape: Border.fromBorderSide(BorderSide.none),
              title: Text(
                '카테고리별 지출',
                style: Theme.of(context).textTheme.titleMedium,
              ),
              children: const [
                ListTile(
                  leading: Icon(Icons.fastfood_outlined),
                  title: Text('식비'),
                  trailing: Text('₩300,000'),
                ),
                ListTile(
                  leading: Icon(Icons.shopping_cart_outlined),
                  title: Text('쇼핑'),
                  trailing: Text('₩200,000'),
                ),
                ListTile(
                  leading: Icon(Icons.house_outlined),
                  title: Text('주거'),
                  trailing: Text('₩150,000'),
                ),
              ],
            ),

            const SizedBox(height: 16),

            // ✅ 결제수단별 지출 (접기/펼치기)
            ExpansionTile(
              initiallyExpanded: true,
              tilePadding: EdgeInsets.zero,
              childrenPadding: EdgeInsets.zero,
              shape: Border.fromBorderSide(BorderSide.none),
              collapsedShape: Border.fromBorderSide(BorderSide.none),
              title: Text(
                '결제수단별 지출',
                style: Theme.of(context).textTheme.titleMedium,
              ),
              children: const [
                ListTile(
                  leading: Icon(Icons.credit_card_outlined),
                  title: Text('하나카드'),
                  trailing: Text('₩300,000'),
                ),
                ListTile(
                  leading: Icon(Icons.credit_card_outlined),
                  title: Text('현대카드'),
                  trailing: Text('₩200,000'),
                ),
                ListTile(
                  leading: Icon(Icons.credit_card_outlined),
                  title: Text('KB카드'),
                  trailing: Text('₩150,000'),
                ),
              ],
            ),
          ],
        ),
      ),
      bottomNavigationBar: Padding(
        padding: const EdgeInsets.fromLTRB(16, 8, 16, 30),
        child: ElevatedButton(
          onPressed: () {
            print('소비내역 업로드 버튼 눌림');
            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (_) =>
                    ExpenseUploadPage(year: widget.year, month: widget.month),
              ),
            );
          },
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.blue,
            foregroundColor: Colors.white,
            padding: const EdgeInsets.symmetric(vertical: 16),
            textStyle: const TextStyle(fontSize: 16),
          ),
          child: const Text('소비내역 업로드'),
        ),
      ),
    );
  }
}
