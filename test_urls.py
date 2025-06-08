#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار جميع الـ URLs للتأكد من إمكانية الوصول إليها
"""

import requests

def test_all_endpoints():
    """اختبار جميع endpoints المتعلقة بإضافة العقارات"""
    
    base_url = "http://localhost:8000"
    
    endpoints_to_test = [
        "/api/properties/add/",
        "/api/properties/add-no-validation/", 
        "/api/properties/add-improved/",
        "/api/test/add-property-simple/"
    ]
    
    test_data = {
        'property_title': 'عقار اختبار',
        'property_description': 'وصف اختبار',
        'property_price_num': 100000,
        'property_area_num': 100
    }
    
    print("🧪 اختبار جميع endpoints إضافة العقارات...")
    print("=" * 60)
    
    for endpoint in endpoints_to_test:
        print(f"\n🔍 اختبار: {endpoint}")
        try:
            response = requests.post(
                f"{base_url}{endpoint}",
                json=test_data,
                headers={'Content-Type': 'application/json'},
                timeout=5
            )
            
            print(f"📊 كود الاستجابة: {response.status_code}")
            
            if response.status_code == 200:
                print("✅ Endpoint متاح ويعمل")
                try:
                    result = response.json()
                    if result.get('success'):
                        print(f"🎯 نجح إنشاء عقار برقم: {result.get('property_id')}")
                except:
                    print("📄 استجابة صحيحة ولكن ليست JSON")
            elif response.status_code == 404:
                print("❌ ERROR: Endpoint غير موجود (404)")
            elif response.status_code == 405:
                print("⚠️  Endpoint موجود ولكن Method غير مسموح")
            else:
                print(f"⚠️  استجابة غير متوقعة: {response.status_code}")
                print(f"📄 المحتوى: {response.text[:200]}...")
            
        except requests.exceptions.ConnectionError:
            print("❌ خطأ: لا يمكن الاتصال بالخادم - تأكد من تشغيل الخادم على localhost:8000")
        except requests.exceptions.Timeout:
            print("❌ خطأ: انتهت مهلة الاتصال")
        except Exception as e:
            print(f"❌ خطأ غير متوقع: {e}")

def test_basic_connection():
    """اختبار الاتصال الأساسي بالخادم"""
    print("\n🌐 اختبار الاتصال الأساسي بالخادم...")
    try:
        response = requests.get("http://localhost:8000/properties/", timeout=5)
        print(f"📊 كود الاستجابة لـ /properties/: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ الخادم يعمل بشكل طبيعي")
        else:
            print("⚠️  الخادم يستجيب ولكن قد تكون هناك مشكلة")
            
    except Exception as e:
        print(f"❌ خطأ في الاتصال: {e}")

if __name__ == "__main__":
    print("🚀 بدء اختبار شامل للـ URLs...")
    test_basic_connection()
    test_all_endpoints()
    print("\n" + "=" * 60)
    print("✅ انتهاء الاختبار") 