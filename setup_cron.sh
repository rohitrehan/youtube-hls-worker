#!/bin/bash

# Define the paths
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
CRON_JOB_SCRIPT="$SCRIPT_DIR/src/cron_job.py"
CRON_JOB_ENTRY="@reboot python3 $CRON_JOB_SCRIPT"
CRON_TEMP_FILE="/tmp/cron_temp"

# Helper function to display usage
usage() {
    echo "Usage: $0 {add|remove}"
    exit 1
}

# Ensure the Python script exists
check_job_script() {
    if [ ! -f "$CRON_JOB_SCRIPT" ]; then
        echo "Error: Job script '$CRON_JOB_SCRIPT' not found."
        exit 1
    fi
}

# Add the cron job
add_cron_job() {
    check_job_script

    # Add the cron job for @reboot
    crontab -l > "$CRON_TEMP_FILE" 2>/dev/null || true
    if ! grep -qF "$CRON_JOB_ENTRY" "$CRON_TEMP_FILE"; then
        echo "$CRON_JOB_ENTRY" >> "$CRON_TEMP_FILE"
        crontab "$CRON_TEMP_FILE"
        echo "Cron job added successfully."
    else
        echo "Cron job already exists."
    fi
}

# Remove the cron job
remove_cron_job() {
    crontab -l > "$CRON_TEMP_FILE" 2>/dev/null || true
    sed -i "\|$CRON_JOB_ENTRY|d" "$CRON_TEMP_FILE"
    crontab "$CRON_TEMP_FILE"
    rm -f "$CRON_TEMP_FILE"
    echo "Cron job removed successfully."
}

# Main script logic
case "$1" in
    add)
        add_cron_job
        ;;
    remove)
        remove_cron_job
        ;;
    *)
        usage
        ;;
esac
