function backupFiles() {
    var sourceDirectory = document.getElementById("sourceDir").value;
    var backupDirectory = document.getElementById("backupDir").value;
    var statusLabel = document.getElementById("statusLabel");

    try {
        // Simulate backup operation (replace with actual logic)
        statusLabel.textContent = "Backup completed successfully!";
    } catch (error) {
        statusLabel.textContent = "Error during backup: " + error;
    }
}
