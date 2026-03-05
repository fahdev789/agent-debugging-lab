
trace = {
    "ticket": "User cannot access account after password reset",

    "model_belief": {
        "active_sessions": True,
        "password_reset_success": True
    },

    "world_state": {
        "active_sessions": False,
        "password_reset_success": True
    },

    "final_action": "Revoke active sessions"
}

print("=== MODEL BELIEF ===")
print(trace["model_belief"])

print("\n=== WORLD STATE ===")
print(trace["world_state"])

print("\n=== CHECK ===")

if trace["model_belief"] != trace["world_state"]:
    print("Mismatch detected → agent acted on incorrect belief")
else:
    print("Belief matches world-state")
