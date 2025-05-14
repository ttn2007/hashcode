import hashlib

# تابع برای تولید هش
def generate_hash(input_string, algorithm='sha256'):
    # انتخاب الگوریتم هش
    if algorithm == 'md5':
        hash_object = hashlib.md5()
    elif algorithm == 'sha1':
        hash_object = hashlib.sha1()
    elif algorithm == 'sha256':
        hash_object = hashlib.sha256()
    else:
        return "الگوریتم هش نامعتبر است."
    
    # تبدیل داده به بایت‌ها و تولید هش
    hash_object.update(input_string.encode())
    return hash_object.hexdigest()

# دریافت ورودی از کاربر
input_string = input("لطفاً یک رشته برای تولید هش وارد کنید: ")

# انتخاب الگوریتم هش از کاربر
print("الگوریتم‌های موجود: md5, sha1, sha256")
algorithm = input("الگوریتم هش مورد نظر را انتخاب کنید: ").lower()

# تولید هش
hashed_string = generate_hash(input_string, algorithm)

print(f"هش تولید شده با الگوریتم {algorithm}: {hashed_string}")