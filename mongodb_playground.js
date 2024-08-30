/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use('forecast');
db.userdefined_collection.deleteMany({});
db.forecast_collection.deleteMany({});
