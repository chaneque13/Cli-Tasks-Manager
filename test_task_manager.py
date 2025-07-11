# test_task_manager.py
import os
import pytest
from test_task_manager import load_tasks, save_tasks

def test_load_and_save_tasks(tmp_path):
    """Test JSON save/load functionality."""
    test_file = tmp_path / "test_tasks.json"
    test_tasks = [{"title": "Test", "description": "Demo"}]
    
    # Save and reload
    save_tasks(test_tasks, file_path=test_file)
    loaded_tasks = load_tasks(file_path=test_file)
    
    assert loaded_tasks == test_tasks