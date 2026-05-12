# Task Manager REST API
A backend REST API built using Django REST Framework and MySQL to manage user-specific tasks securely.
# Tech Stack
- Python
- Django
- Django REST Framework
- MySQL
# Features 
- User registration and login with token authentication
- Create, read, update, delete tasks
- Users can only access their own tasks
# API Endpoints
Endpoint | Method | Description |

/api/register/ | POST | Register new user |

/api/login/ | POST | Login and get token |

/api/tasks/ | POST | Create new task |

/api/tasks/ | GET | List all tasks |

/api/tasks/<id>/ | GET | Get single task |

/api/tasks/<id>/ | PUT | Update task |

/api/tasks/<id>/ | DELETE | Delete task |
# Setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
