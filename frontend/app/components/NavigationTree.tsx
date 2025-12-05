'use client'

import React from 'react';
import Link from "next/link";
import {useSearch} from "@/context/SearchContext";

const NavigationTree = () => {
    const {search, setSearch} = useSearch();

    return (
        <nav className="bg-white border-b border-gray-200">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">

                {/* Logo */}
                <div className="flex items-center">
                    <span className="text-xl font-semibold text-gray-800">MyApp</span>
                </div>

                {/* Search */}
                <div className="hidden md:flex items-center w-1/2">
                    <input
                        type="text"
                        placeholder="Search by Agent, Customer, or Ticket Number"
                        className="w-full px-3 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        onChange={(e) => setSearch(e.target.value)}
                        value={search}
                    />
                </div>

                {/* Right Links */}
                <div className="flex items-center space-x-4">
                    <a href="#" className="text-gray-700 hover:text-blue-600">Home</a>
                    <a href="#" className="text-gray-700 hover:text-blue-600">About</a>
                </div>
            </div>

            {/* Mobile Search Bar */}
            <div className="md:hidden px-4 pb-2">
                <input
                    type="text"
                    placeholder="Search by Agent, Customer, or Ticket Number"
                    className="w-full px-3 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
            </div>
        </nav>
    );
};

export default NavigationTree;