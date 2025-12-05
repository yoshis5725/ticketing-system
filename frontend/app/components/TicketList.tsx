'use client'

import React, {useEffect, useState} from 'react';
import Link from "next/link";
import axios from "axios";
import {Ticket} from "@/utils/Types";
import {formatDate} from "@/utils/helpers";
import {useSearch} from "@/context/SearchContext";

const TicketList = () => {
    const {search} = useSearch();
    const [tickets, setTickets] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)


    /**
     * Retrieving the list of ALL tickets on page load. If there is an error, will display that error instead of the
     * tickets.
     */
    useEffect(() => {
        const fetchTickets = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/tickets/filter/')
                setTickets(response.data)
            } catch (error) {
                setError((error as Error).message)
                console.error('An error fetching tickets occurred!', error)
            } finally {
                setLoading(false)
            }
        }
        fetchTickets()
    }, [])


    /**
     * Filtering the tickets based on a users search. Returning back the matching rowing that meet the users
     * search criteria
     * Search by:
     * - agent
     * - customer
     * - ticket number
     */
    const filteredTickets = tickets.filter(
        (ticket: Ticket) =>
            ticket.ticket_number.toLowerCase().includes(search.toLowerCase()) ||
            ticket.agent_full_name.toLowerCase().includes(search.toLowerCase()) ||
            ticket.customer.full_name.toLowerCase().includes(search.toLowerCase())
    )

    return (
        <div className="overflow-x-auto">
            <table className="min-w-full border border-gray-200 rounded-lg overflow-hidden">
                <thead className="bg-gray-100">
                <tr>
                    <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 border-b">
                        Ticket Number
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 border-b">
                        Ticket Status
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 border-b">
                        Assigned Agent
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 border-b">
                        Customer
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 border-b">
                        Created Date
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 border-b">
                        Target Date
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 border-b">
                        Urgency
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 border-b">
                        Group Responsible
                    </th>
                </tr>
                </thead>

                <tbody>
                {
                    filteredTickets.map((ticket: Ticket) => (
                        <tr key={ticket.id} className="odd:bg-white even:bg-gray-50">
                            <td className="px-4 py-2 border-b">
                                <Link href={`/tickets/${ticket.id}`}
                                      className="text-sm font-semibold text-green-800 hover:text-gray-900">
                                    {ticket.ticket_number}
                                </Link>
                            </td>
                            <td className="px-4 py-2 border-b">{ticket.status_display}</td>
                            <td className="px-4 py-2 border-b">{ticket.agent_full_name}</td>
                            <td className="px-4 py-2 border-b">{ticket.customer.full_name}</td>
                            <td className="px-4 py-2 border-b">{formatDate(ticket.created_at)}</td>
                            <td className="px-4 py-2 border-b">{formatDate(ticket.target_date)}</td>
                            <td className="px-4 py-2 border-b">{ticket.urgency_display}</td>
                            <td className="px-4 py-2 border-b">{ticket.group.group_name}</td>
                        </tr>
                    ))
                }
                </tbody>
            </table>
        </div>
    );
};

export default TicketList;