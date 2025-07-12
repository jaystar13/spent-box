import 'package:flutter/material.dart';

class ExpenseUploadPage extends StatefulWidget {
  final int year;
  final int month;

  const ExpenseUploadPage({super.key, required this.year, required this.month});

  @override
  State<ExpenseUploadPage> createState() => _ExpenseUploadPageState();
}

class _ExpenseUploadPageState extends State<ExpenseUploadPage> {
  bool _isAnalyzing = false;

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
                _buildStepCircle(context, "1", "업로드", !_isAnalyzing),
                _buildLine(),
                _buildStepCircle(context, "2", "분석", _isAnalyzing),
                _buildLine(),
                _buildStepCircle(context, "3", "완료", false),
              ],
            ),
            const SizedBox(height: 32),

            _isAnalyzing ? _buildAnalysisSection() : _buildUploadSection(),

            const Spacer(),

            // 하단 버튼
            Row(
              children: [
                if (_isAnalyzing)
                  TextButton.icon(
                    onPressed: () {
                      setState(() {
                        _isAnalyzing = false; // 또는 이전 단계로
                      });
                    },
                    icon: const Icon(Icons.arrow_back),
                    label: const Text('이전'),
                  ),
                const Spacer(),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      _isAnalyzing = true;
                    });
                  },
                  child: Text(_isAnalyzing ? '완료' : '분석'),
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

  Widget _buildUploadSection() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
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
              Icon(Icons.cloud_upload_outlined, size: 48, color: Colors.blue),
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
      ],
    );
  }

  Widget _buildAnalysisSection() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('업로드 분석'),
        const SizedBox(height: 8),
        _buildCategoryCard('식비', 80000, ['GS편의점', '스타벅스']),
        _buildCategoryCard('쇼핑', 120000, ['현대백화점', '루이비통']),
        _buildCategoryCard('미분류', 552100, ['신라호텔', '백다방']),
      ],
    );
  }

  Widget _buildCategoryCard(String title, int amount, List<String> tags) {
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      child: ExpansionTile(
        title: Text('$title ${_formatCurrency(amount)}'),
        shape: Border.fromBorderSide(BorderSide.none),
        collapsedShape: Border.fromBorderSide(BorderSide.none),
        children: [
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16),
            child: Align(
              alignment: Alignment.centerLeft,
              child: Wrap(
                spacing: 8,
                runSpacing: 8,
                children: tags
                    .map(
                      (tag) => Chip(
                        label: Text(tag),
                        backgroundColor: Colors.grey.shade200,
                      ),
                    )
                    .toList(),
              ),
            ),
          ),
          const SizedBox(height: 12),
        ],
      ),
    );
  }

  String _formatCurrency(int amount) {
    return '${amount.toString().replaceAllMapped(RegExp(r'(\d)(?=(\d{3})+(?!\d))'), (match) => '${match[1]},')}원';
  }
}
