import 'package:flutter/material.dart';

class CategoryItemsPage extends StatefulWidget {
  final int year;
  final int month;

  const CategoryItemsPage({super.key, required this.year, required this.month});

  @override
  State<CategoryItemsPage> createState() => _CategoryItemsPageState();
}

class _CategoryItemsPageState extends State<CategoryItemsPage> {
  final Map<String, List<String>> categoryChips = {
    '미분류': ['내역1', '내역2'],
    '식비': ['식비항목1', '식비항목2'],
    '쇼핑': ['쇼핑항목1', '쇼핑항목2'],
  };

  void moveToCategory(String chip, String targetCategory) {
    if (!categoryChips[targetCategory]!.contains(chip)) {
      setState(() {
        categoryChips['미분류']?.remove(chip);
        categoryChips[targetCategory]?.add(chip);
      });
    }
  }

  void removeFromCategory(String chip, String category) {
    if (category != '미분류') {
      setState(() {
        categoryChips[category]?.remove(chip);
        categoryChips['미분류']?.add(chip);
      });
    }
  }

  void _showChipSelectionDialog(
    BuildContext context,
    String targetCategory,
  ) async {
    final availableChips = List<String>.from(categoryChips['미분류']!);
    final Set<String> selectedChips = {};

    await showDialog<void>(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text('항목 선택'),
          content: StatefulBuilder(
            builder: (context, setState) {
              return SingleChildScrollView(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: availableChips.map((chip) {
                    final isSelected = selectedChips.contains(chip);
                    return CheckboxListTile(
                      title: Text(chip),
                      value: isSelected,
                      onChanged: (bool? checked) {
                        setState(() {
                          if (checked == true) {
                            selectedChips.add(chip);
                          } else {
                            selectedChips.remove(chip);
                          }
                        });
                      },
                    );
                  }).toList(),
                ),
              );
            },
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: Text('취소'),
            ),
            ElevatedButton(
              onPressed: () {
                for (final chip in selectedChips) {
                  moveToCategory(chip, targetCategory);
                }
                Navigator.of(context).pop();
              },
              child: Text('추가'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('카테고리 구성항목 수정')),
      body: ListView(
        children: categoryChips.entries.map((entry) {
          final isUnclassified = entry.key == '미분류';
          return buildCategoryBox(
            entry.key,
            entry.value,
            isUnclassified
                ? null
                : (chip) => removeFromCategory(chip, entry.key),
            isUnclassified
                ? null
                : () {
                    _showChipSelectionDialog(context, entry.key);
                  },
          );
        }).toList(),
      ),
    );
  }
}

Widget buildCategoryBox(
  String title,
  List<String> chips,
  void Function(String)? onRemove,
  VoidCallback? onAdd,
) {
  return Padding(
    padding: const EdgeInsets.all(12),
    child: Stack(
      clipBehavior: Clip.none,
      children: [
        Container(
          width: double.infinity,
          height: 180, // Approx. 5 rows height
          padding: const EdgeInsets.only(
            top: 20,
            left: 12,
            right: 12,
            bottom: 12,
          ),
          decoration: BoxDecoration(
            border: Border.all(color: Colors.grey.shade300),
            borderRadius: BorderRadius.circular(12),
            color: Colors.white,
          ),
          child: SingleChildScrollView(
            child: Wrap(
              spacing: 8,
              runSpacing: 8,
              children: [
                ...chips.map(
                  (chip) => InputChip(
                    label: Text(chip),
                    onDeleted: onRemove == null ? null : () => onRemove(chip),
                  ),
                ),
                if (onAdd != null)
                  ActionChip(label: Icon(Icons.add), onPressed: onAdd),
              ],
            ),
          ),
        ),
        Positioned(
          top: -10,
          left: 16,
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 8),
            color: Colors.white,
            child: Text(
              title,
              style: TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.bold,
                color: Colors.black87,
              ),
            ),
          ),
        ),
      ],
    ),
  );
}
