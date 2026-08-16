"""
Testy jednostkowe weryfikacji kompletności danych w warstwie Bronze (run_audit).
"""
import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db import DatabaseManager

class TestCompletenessAudit(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "test_audit.db")
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db_manager = DatabaseManager(db_path=self.db_path)
        self.run_id = "test_run_audit_1"

    def tearDown(self):
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except Exception:
                pass

    def test_save_and_retrieve_run_audit(self):
        """Test zapisu i odczytu metryk kompletności z tabeli run_audit"""
        self.db_manager.save_run_audit(self.run_id, "otodom", expected_total=126, saved_bronze=126)
        self.db_manager.save_run_audit(self.run_id, "adresowo", expected_total=133, saved_bronze=133)

        audits = self.db_manager.get_run_audits(self.run_id)
        self.assertEqual(len(audits), 2)

        audit_map = {a["source_portal"]: a for a in audits}
        self.assertEqual(audit_map["otodom"]["completeness_pct"], 100.0)
        self.assertEqual(audit_map["adresowo"]["completeness_pct"], 100.0)
        self.assertEqual(audit_map["adresowo"]["saved_bronze"], 133)

if __name__ == "__main__":
    unittest.main()
