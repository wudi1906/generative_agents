import mysql.connector
import json
from typing import Dict, List, Optional

class DBManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="192.168.50.137",
            port=3306,
            user="root",  # 替换为实际的用户名
            password="123456",  # 替换为实际的密码
            database="wenjuan"  # 替换为实际的数据库名
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def create_human(self, name: str, age: int, gender: str, 
                    attributes: Dict, father_id: Optional[int] = None, 
                    mother_id: Optional[int] = None) -> int:
        """创建新的数字人"""
        query = """
        INSERT INTO digital_humans 
        (name, age, gender, attributes, father_id, mother_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (
            name, 
            age, 
            gender,
            json.dumps(attributes),
            father_id,
            mother_id
        ))
        self.connection.commit()
        return self.cursor.lastrowid

    def get_human_by_id(self, human_id: int) -> Dict:
        """根据ID获取数字人信息"""
        query = "SELECT * FROM digital_humans WHERE id = %s"
        self.cursor.execute(query, (human_id,))
        return self.cursor.fetchone()

    def get_human_by_name(self, name: str) -> Dict:
        """根据名字获取数字人信息"""
        query = "SELECT * FROM digital_humans WHERE name = %s"
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()

    def get_all_humans(self) -> List[Dict]:
        """获取所有数字人列表"""
        query = "SELECT * FROM digital_humans"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_human(self, human_id: int, **kwargs) -> bool:
        """更新数字人信息"""
        valid_fields = {'name', 'age', 'gender', 'attributes', 'father_id', 'mother_id'}
        updates = []
        values = []
        
        for key, value in kwargs.items():
            if key in valid_fields:
                updates.append(f"{key} = %s")
                values.append(value if key != 'attributes' else json.dumps(value))
        
        if not updates:
            return False
            
        query = f"""
        UPDATE digital_humans 
        SET {', '.join(updates)}
        WHERE id = %s
        """
        values.append(human_id)
        
        self.cursor.execute(query, tuple(values))
        self.connection.commit()
        return True

    def get_family(self, human_id: int) -> Dict:
        """获取家庭信息"""
        human = self.get_human_by_id(human_id)
        if not human:
            return {}
            
        family = {
            "self": human,
            "father": self.get_human_by_id(human['father_id']) if human['father_id'] else None,
            "mother": self.get_human_by_id(human['mother_id']) if human['mother_id'] else None,
        }
        return family

    def __del__(self):
        """关闭数据库连接"""
        if hasattr(self, 'cursor'):
            self.cursor.close()
        if hasattr(self, 'connection'):
            self.connection.close() 