#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار endpoint باستخدام البيانات الفعلية التي يرسلها المستخدم
"""

import requests
import json

def test_with_your_exact_data():
    """اختبار باستخدام البيانات التي ترسلها أنت بالضبط"""
    
    # ضع هنا نفس البيانات التي ترسلها من Frontend
    your_data = {
        "property_title": "شقة للبيع في منطقة راقية",
        "property_description": "شقة مفروشة بالكامل في موقع متميز",
        "property_price_num": 750000,
        "property_area_num": 120,
        "property_photo": "https://example.com/property.jpg",
        "property_location_1": "محافظة جديدة تماماً",
        "property_location_2": "منطقة لا توجد في قاعدة البيانات",
        "property_type_1_ID": 1,
        "payment_method_ID": 1,
        "property_overlooking_ID": 1,
        "Advertiser_type_ID": 1
    }
    
    print("🧪 اختبار endpoint باستخدام بياناتك الفعلية...")
    print("=" * 60)
    print(f"📤 البيانات المرسلة:")
    print(json.dumps(your_data, ensure_ascii=False, indent=2))
    print("=" * 60)
    
    try:
        # اختبار على localhost أولاً
        print("\n🔍 اختبار على الخادم المحلي...")
        response = requests.post(
            "http://localhost:8000/api/properties/add-no-validation/",
            json=your_data,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Test Script)'
            },
            timeout=10
        )
        
        print(f"📊 كود الاستجابة: {response.status_code}")
        print(f"📄 الاستجابة: {response.text}")
        
        if response.status_code == 200:
            print("✅ نجح على الخادم المحلي!")
            result = response.json()
            print(f"🎯 معرف العقار الجديد: {result.get('property_id')}")
            print(f"📍 المحافظة المحفوظة: {result.get('location_1')}")
            print(f"📍 المنطقة المحفوظة: {result.get('location_2')}")
        elif response.status_code == 404:
            print("❌ ERROR: Endpoint غير موجود (404)")
            print("🔧 الحلول المقترحة:")
            print("   1. تأكد من تشغيل الخادم: python manage.py runserver")
            print("   2. تأكد من المسار: /api/properties/add-no-validation/")
        else:
            print(f"⚠️  خطأ غير متوقع: {response.status_code}")
            print(f"📄 تفاصيل الخطأ: {response.text}")
        
    except requests.exceptions.ConnectionError:
        print("❌ لا يمكن الاتصال بالخادم المحلي")
        print("🔧 تأكد من تشغيل: python manage.py runserver 0.0.0.0:8000")
    except Exception as e:
        print(f"❌ خطأ: {e}")
    
    # اختبار على Render إذا كان متاحاً
    print("\n🔍 اختبار على خادم Render...")
    try:
        response = requests.post(
            "https://graduation-project-1-0a1a.onrender.com/api/properties/add-no-validation/",
            json=your_data,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Test Script)'
            },
            timeout=15
        )
        
        print(f"📊 كود الاستجابة: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ نجح على خادم Render!")
            result = response.json()
            print(f"🎯 معرف العقار الجديد: {result.get('property_id')}")
        elif response.status_code == 404:
            print("❌ ERROR: Endpoint غير موجود على Render")
            print("🔧 يجب رفع الكود الجديد إلى GitHub وانتظار إعادة النشر")
        else:
            print(f"⚠️  خطأ على Render: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ لا يمكن الاتصال بخادم Render")
    except requests.exceptions.Timeout:
        print("❌ انتهت مهلة الاتصال بخادم Render")
    except Exception as e:
        print(f"❌ خطأ Render: {e}")

def test_minimal_data():
    """اختبار بأقل البيانات المطلوبة"""
    
    minimal_data = {
        "property_title": "عقار تجريبي",
        "property_description": "وصف تجريبي",
        "property_price_num": 100000,
        "property_area_num": 100
    }
    
    print("\n🧪 اختبار بأقل البيانات المطلوبة...")
    try:
        response = requests.post(
            "http://localhost:8000/api/properties/add-no-validation/",
            json=minimal_data,
            headers={'Content-Type': 'application/json'},
            timeout=5
        )
        
        if response.status_code == 200:
            print("✅ نجح الاختبار البسيط!")
            result = response.json()
            print(f"🎯 معرف العقار: {result.get('property_id')}")
        else:
            print(f"❌ فشل: {response.status_code}")
            
    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    print("🚀 اختبار شامل لبياناتك الفعلية...")
    test_with_your_exact_data()
    test_minimal_data()
    print("\n" + "=" * 60)
    print("✅ انتهاء الاختبار") 