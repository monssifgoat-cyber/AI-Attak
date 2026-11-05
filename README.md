# فريق اختبار الاختراق الآلي (Pentest Agent Team)

فريق وكلاء ذكاء اصطناعي لاختبار اختراق **مصرّح به** على نسخة/Staging يزوّدها العميل.

## الوكلاء
1. **Recon** — استطلاع: منافذ، تقنيات، endpoints (nmap, httpx, katana)
2. **Scanner** — فحص الثغرات (nuclei, OWASP ZAP, sqlmap)
3. **Exploiter** — استغلال كامل للثغرات المؤكدة حتى الوصول/الصلاحيات القصوى
4. **Reporter** — تقرير CVSS احترافي (HTML/PDF) مع أين نجح وأين فشل

## التشغيل محلياً أو على سيرفر
```bash
# 1) شغّل Ollama (للتحليل الخاص)
docker run -d -p 11434:11434 ollama/ollama
docker exec <id> ollama pull qwen2.5:14b

# 2) ابنِ صورة الفريق
docker compose build

# 3.1) شغّل ZAP (فحص شامل عبر API)
docker compose up -d zap

# 3.2) شغّل المهمة
docker compose run --rm team python main.py --config config.yaml
```

## النشر المجاني (جهازك ضعيف)
- **Oracle Cloud Free Tier** (24GB RAM): انسخ المشروع، شغّل docker compose — الأفضل للمهام الطويلة
- **Hugging Face Spaces**: ارفع المشروع كـ Space من نوع Docker

## ⚠️ حماية مهنية
- عدّل `scope.targets` فقط لنطاق العميل المكتوب في العقد
- الافتراضي: استغلال كامل لكن غير مُتلف (لا حذف بيانات)
- كل النتائج تُحفظ في `output/` وتُرفق للعميل
