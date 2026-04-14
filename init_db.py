import os
from app import app, db, User, Group, Subject

def init_database():
    """Initialize database with tables and default data"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # Check if admin user exists
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            # Create default admin user
            admin_user = User(
                username='admin',
                password_hash='pbkdf2:sha256:260000$salt$hash',  # Will be updated below
                first_name='Admin',
                last_name='User',
                is_admin=True,
                is_group_leader=False,
                needs_password_change=False
            )
            admin_user.set_password('admin123')
            db.session.add(admin_user)
            print("Admin user created!")
        
        # Create default groups if they don't exist
        default_groups = ['Group 1', 'Group 2', 'Group 3']
        for group_name in default_groups:
            existing_group = Group.query.filter_by(name=group_name).first()
            if not existing_group:
                group = Group(name=group_name, description=f'Default {group_name}')
                db.session.add(group)
        
        # Create default subjects if they don't exist
        default_subjects = [
            ('Huquq', 'Huquq fanlari'),
            ('Ingliz tili', 'English language'),
            ('Tarix', 'History'),
            ('Ona tili', 'Uzbek language'),
            ('Matematika', 'Mathematics')
        ]
        
        for subject_name, description in default_subjects:
            existing_subject = Subject.query.filter_by(name=subject_name).first()
            if not existing_subject:
                subject = Subject(name=subject_name, description=description)
                db.session.add(subject)
        
        db.session.commit()
        print("Database initialization completed!")

if __name__ == '__main__':
    init_database()
