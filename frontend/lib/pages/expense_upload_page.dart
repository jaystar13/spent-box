import 'package:flutter/material.dart';
import 'package:frontend/pages/expense_analysis_page.dart';

class ExpenseUploadPage extends StatefulWidget {
  final int year;
  final int month;

  const ExpenseUploadPage({super.key, required this.year, required this.month});

  @override
  State<ExpenseUploadPage> createState() => _ExpenseUploadPageState();
}

class _ExpenseUploadPageState extends State<ExpenseUploadPage> {
  @override
  Widget build(BuildContext context) {
    String selectedBank = 'AA 카드';

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
                _buildStepCircle(context, "2", "분석", false),
                _buildLine(),
                _buildStepCircle(context, "3", "완료", false),
              ],
            ),
            const SizedBox(height: 32),

            Text('금융기관 선택'),
            const SizedBox(height: 8),
            Wrap(
              spacing: 16,
              children: [
                ChoiceChip(label: Text("AA 카드"), selected: true),
                ChoiceChip(label: Text("BB 은행"), selected: false),
                ChoiceChip(label: Text("CC 카드"), selected: false),
              ],
            ),
            const SizedBox(height: 32),

            // 파일 업로드 박스
            Container(
              width: double.infinity,
              padding: const EdgeInsets.symmetric(vertical: 40),
              decoration: BoxDecoration(
                border: Border.all(color: Colors.grey.shade300),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: const [
                  Icon(
                    Icons.cloud_upload_outlined,
                    size: 48,
                    color: Colors.blue,
                  ),
                  SizedBox(height: 8),
                  Text.rich(
                    TextSpan(
                      children: [
                        TextSpan(
                          text: 'Link',
                          style: TextStyle(color: Colors.blue),
                        ),
                        TextSpan(text: ' or drag and drop'),
                      ],
                    ),
                  ),
                  SizedBox(height: 4),
                  Text(
                    'SVG, PNG, JPG or GIF (max. 3MB)',
                    style: TextStyle(color: Colors.grey),
                  ),
                ],
              ),
            ),

            const Spacer(),

            // 하단 버튼
            Row(
              children: [
                const Spacer(),
                ElevatedButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (_) => ExpenseAnalysisPage(
                          year: widget.year,
                          month: widget.month,
                        ),
                      ),
                    );
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.blue,
                    foregroundColor: Colors.white,
                    padding: EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text('분석'),
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
