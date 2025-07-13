import 'package:flutter/material.dart';

class ExpenseAnalysisPage extends StatefulWidget {
  final int year;
  final int month;

  const ExpenseAnalysisPage({
    super.key,
    required this.year,
    required this.month,
  });

  @override
  State<ExpenseAnalysisPage> createState() => _ExpenseUploadPageState();
}

class _ExpenseUploadPageState extends State<ExpenseAnalysisPage> {
  @override
  Widget build(BuildContext context) {
    //String selectedBank = 'AA 카드';

    return Scaffold(
      appBar: AppBar(title: Text('업로드 - ${widget.year}년 ${widget.month}월')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              '소비내역 업로드',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 16),

            // 단계 표시
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                _buildStepCircle(context, "1", "업로드", true),
                _buildLine(),
                _buildStepCircle(context, "2", "분석", true),
                _buildLine(),
                _buildStepCircle(context, "3", "완료", false),
              ],
            ),
            const SizedBox(height: 32),

            Text(
              '업로드 분석',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            ),

            // 하단 버튼
            Row(
              children: [
                const Spacer(),
                ElevatedButton(
                  onPressed: () {},
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.blue,
                    foregroundColor: Colors.white,
                    padding: EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text('완료'),
                      SizedBox(width: 4),
                      Icon(Icons.arrow_forward),
                    ],
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildStepCircle(
    BuildContext context,
    String step,
    String label,
    bool active,
  ) {
    return Column(
      children: [
        CircleAvatar(
          radius: 16,
          backgroundColor: active ? Colors.blue : Colors.grey.shade300,
          child: Text(
            step,
            style: const TextStyle(color: Colors.white, fontSize: 14),
          ),
        ),
        const SizedBox(height: 4),
        Text(
          label,
          style: TextStyle(color: active ? Colors.black : Colors.grey),
        ),
      ],
    );
  }

  Widget _buildLine() {
    return const Padding(
      padding: EdgeInsets.symmetric(horizontal: 8),
      child: SizedBox(width: 24, child: Divider(thickness: 1)),
    );
  }
}
