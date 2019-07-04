Steps to recreate issues:
1. Run `./runme.sh` 
    * Note that this script uses `python3` to create a virtual environment (3.5+ is required)
2. Access the admin interface from your browser on `http://localhost:8000/admin`
3. Login as a super user (username: `test`, password: `pass`)
4. Navigate to the `Bar` admin changelist page (`http://localhost:8000/admin/app/bar/`). **Note that `BarAdmin` IS NOT a subclass of `VersionAdmin`.**
5. Change `thing` for one record and `stuff` for the other and click `Save`.
![image](https://github.com/Palisand/django_reversion_issue_tester/blob/master/screenshots/changelist_changes.png?raw=true)
6. Observe that in the history page for the record that had `thing` changed, the action is listed as "Changed thing". Also observe that in the history for the record that had `stuff` changed, the action is listed as "Changed stuff".
![image](https://github.com/Palisand/django_reversion_issue_tester/blob/master/screenshots/bar_1_history.png?raw=true)
![image](https://github.com/Palisand/django_reversion_issue_tester/blob/master/screenshots/bar_2_history.png?raw=true)
7. Navigate to the `Foo` admin changelist page (`http://localhost:8000/admin/app/bar/`). **Note that `FooAdmin` IS a subclass of `VersionAdmin`.**
8. Repeat step 5, this time for the `Foo` records.
9. (ISSUE #1) Observe that in the history pages for **both** records, the action is the same.
![image](https://github.com/Palisand/django_reversion_issue_tester/blob/master/screenshots/foo_1_history.png?raw=true)
![image](https://github.com/Palisand/django_reversion_issue_tester/blob/master/screenshots/foo_2_history.png?raw=true)
10. From the `Foo` admin changelist page, make another set of changes that affects both records.
11. From the history page of **any one** `Foo` record, revert to the previous set of changes (i.e. the version directly after the initial version).
12. (ISSUE #2) From the changelist page, observe that **both** records have been reverted.
13. (ISSUE #3) Observe that only one history page has been updated in spite of both records being affected. 
![image](https://github.com/Palisand/django_reversion_issue_tester/blob/master/screenshots/foo_1_history_post_revert.png?raw=true)
![image](https://github.com/Palisand/django_reversion_issue_tester/blob/master/screenshots/foo_2_history_post_revert.png?raw=true)

Issues 2 and 3 may be resolved by updating the history of all records that are part of a revision or by ensuring that only one record is reverted.

Note: reverting to the initial version will affect a single record.
