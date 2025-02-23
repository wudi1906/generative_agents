from reverie.backend.utils.db_manager import DBManager

def main():
    # 创建数据库管理器实例
    db = DBManager()

    # 准备 Jack 的数据
    attributes = {
        "hobbies": ["sports", "gaming"],
        "pet_name": "Max",
        "personality": "outgoing",
        "occupation": "student"
    }

    try:
        # 创建 Jack 的记录
        human_id = db.create_human(
            name="Jack",
            age=18,
            gender="male",
            attributes=attributes
        )
        print(f"Successfully created human with ID: {human_id}")

        # 验证数据是否插入成功
        jack = db.get_human_by_name("Jack")
        print("Inserted data:", jack)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 