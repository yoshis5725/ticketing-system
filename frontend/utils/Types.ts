

export type Ticket = {
    id: string;
    title: string;
    ticket_number: string;
    description: string;
    attachment: File | null;
    created_at: Date;
    target_date: Date;
    urgency_display: 'low' | 'moderate' | 'high' | 'critical';
    agent_full_name: string;
    status_display: 'open' | 'closed' | 'assigned' | 'appointment_set';
    group: {
        id: string;
        group_name: string;
    }
    customer: {
        id: string;
        full_name: string;
    }
}